"""
Evaluator module for managing Fireworks evaluators.

This module provides the Evaluator class which handles the creation and management
of evaluators on the Fireworks platform. Evaluators are created from reward functions
and can be reused across multiple evaluation jobs.

The Evaluator class follows the same pattern as EvaluationJob, providing:
- Object-oriented interface for evaluator management
- Automatic versioning of evaluators
- Reuse of identical evaluators to avoid duplication
- Integration with the Fireworks Gateway

Example usage:
    from fireworks import Evaluator
    from fireworks.gateway import Gateway

    gateway = Gateway()
    evaluator = Evaluator(gateway=gateway, reward_function=my_reward_function)
    evaluator.sync()  # Creates or finds existing evaluator
    print(f"Evaluator URL: {evaluator.url}")
"""

import ast
import inspect
import json
import os
import re
from datetime import datetime
from typing import Callable, List, Optional

from fireworks._util import (
    dedent_code,
    find_requirements_or_pyproject,
    get_requirements_from_pyproject_or_requirements_txt,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.evaluator_pb2 import (
    Evaluator as SyncEvaluator,
    Criterion as SyncCriterion,
    CodeSnippets as SyncCodeSnippets,
    RollupSettings as SyncRollupSettings,
    CreateEvaluatorRequest as SyncCreateEvaluatorRequest,
    ListEvaluatorsRequest as SyncListEvaluatorsRequest,
    PreviewEvaluatorRequest as SyncPreviewEvaluatorRequest,
    PreviewEvaluatorResponse as SyncPreviewEvaluatorResponse,
)
from fireworks.gateway import Gateway
from fireworks._logger import logger


class Evaluator:
    VERSION_DELIMITER = "-v"

    def __init__(self, gateway: Gateway, reward_function: Callable):
        """
        An Evaluator class that manages the creation and retrieval of evaluators on Fireworks.

        Args:
            gateway: The Fireworks Gateway instance
            reward_function: A callable decorated with @reward_function
        """
        self._gateway = gateway
        self._reward_function = reward_function
        self._proto: Optional[SyncEvaluator] = None

        # Validate the reward function
        self._validate_reward_function()

    @property
    def _reward_function_name(self) -> str:
        """Get the name of the reward function"""
        return self._reward_function.__name__

    @property
    def _unwrapped_reward_function(self) -> Callable:
        """Unwrap the reward function completely and cache the result"""
        # unwrap until not unwrappable
        prev_unwrapped = None
        unwrapped = inspect.unwrap(self._reward_function)
        while unwrapped != prev_unwrapped:
            prev_unwrapped = unwrapped
            unwrapped = inspect.unwrap(unwrapped)
        return unwrapped

    @property
    def _reward_function_relative_path(self) -> str:
        """Get the relative path of the reward function"""
        return self._get_relative_path(self._reward_function_file_path)

    @property
    def _reward_function_file_path(self) -> str:
        """Get the file path of the reward function"""
        file_path = inspect.getsourcefile(self._unwrapped_reward_function)
        if not file_path:
            raise ValueError("Reward function must be defined in a file")
        return file_path

    @property
    def _reward_function_source(self) -> str:
        """Get the source code of the reward function itself only"""
        return inspect.getsource(self._unwrapped_reward_function)

    @property
    def _reward_function_file_source(self) -> str:
        """Get the source for the entire file that hosts the reward function"""
        with open(self._reward_function_file_path, "r", encoding="utf-8") as f:
            return f.read()

    @property
    def _reward_function_file_name(self) -> str:
        """Get the file name of the reward function"""
        file_name = os.path.basename(self._reward_function_file_path)
        return file_name

    def _validate_reward_function(self):
        """Validate that the reward function is properly decorated"""

        # if source does not decorate with @reward_function, raise an error
        if not self._reward_function_source.startswith("@reward_function"):
            raise ValueError("Reward function must be decorated with @reward_function")

    def _get_sibling_and_child_files(self) -> List[str]:
        """
        Recursively find all sibling and child files relative to the reward function file.
        Returns absolute paths of Python files (.py) in the same directory and subdirectories.

        Also ignore a default set of files that are probably not relevant to the
        reward function (hidden, node_modules, .git, etc.)
        """
        reward_function_dir = os.path.dirname(self._reward_function_file_path)
        all_files = []

        # Walk through the directory and all subdirectories
        for root, dirs, files in os.walk(reward_function_dir):
            # Skip hidden directories and common non-source directories
            dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ["__pycache__", "node_modules", ".git"]]

            for file in files:
                if not file.startswith("."):
                    file_path = os.path.join(root, file)
                    all_files.append(file_path)

        return all_files

    def _get_relative_path(self, file_path: str) -> str:
        """
        Get the relative path of a file from the reward function's directory.

        Args:
            file_path: Absolute path to the file

        Returns:
            Relative path from the reward function's directory
        """
        reward_function_dir = os.path.dirname(self._reward_function_file_path)
        return os.path.relpath(file_path, reward_function_dir)

    def _get_file_source(self, file_path: str) -> str:
        """
        Read and return the source code of a file.

        Args:
            file_path: Absolute path to the file

        Returns:
            Source code of the file
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            logger.warning(f"Could not read file {file_path}: {e}")
            return ""

    def _convert_relative_imports(self, source_code: str, file_path: str) -> str:
        """
        Convert relative imports to absolute imports in Python source code.

        Args:
            source_code: The Python source code
            file_path: Absolute path to the file (used to determine package structure)

        Returns:
            Source code with relative imports converted to absolute imports
        """
        try:
            # Parse the source code into an AST
            tree = ast.parse(source_code)
        except SyntaxError:
            # If we can't parse the code, return it unchanged
            logger.warning(f"Could not parse Python code in {file_path}, skipping import conversion")
            return source_code

        # Get the package path for this file relative to the reward function directory
        reward_function_dir = os.path.dirname(self._reward_function_file_path)
        relative_file_path = os.path.relpath(file_path, reward_function_dir)

        # Convert file path to package path (remove .py extension and replace / with .)
        if relative_file_path.endswith(".py"):
            # Convert path to package notation
            package_path = relative_file_path[:-3].replace(os.sep, ".")
            # Remove __init__ from package path if present
            if package_path.endswith(".__init__"):
                package_path = package_path[:-9]
            current_package = package_path
        else:
            current_package = ""

        # Track modifications to make
        modifications = []

        # Walk through all import nodes
        for node in ast.walk(tree):
            if isinstance(node, (ast.ImportFrom, ast.Import)):
                if isinstance(node, ast.ImportFrom) and node.level > 0:
                    # This is a relative import
                    relative_level = node.level
                    module_name = node.module or ""

                    # Calculate the absolute module name
                    if current_package:
                        package_parts = current_package.split(".")
                        # Go up 'level' number of packages
                        if relative_level > len(package_parts):
                            # Can't go up more levels than we have, skip this import
                            continue

                        if relative_level == len(package_parts) + 1:
                            # Going to parent of root, assume empty base
                            absolute_module = module_name
                        else:
                            base_package_parts = (
                                package_parts[:-relative_level] if relative_level <= len(package_parts) else []
                            )
                            base_package = ".".join(base_package_parts) if base_package_parts else ""

                            if module_name:
                                absolute_module = f"{base_package}.{module_name}" if base_package else module_name
                            else:
                                absolute_module = base_package
                    else:
                        # We're at root level
                        absolute_module = module_name

                    # Store the modification info
                    modifications.append(
                        {
                            "lineno": node.lineno,
                            "col_offset": node.col_offset,
                            "original_level": relative_level,
                            "original_module": node.module,
                            "absolute_module": absolute_module,
                            "names": [alias.name for alias in node.names] if node.names else [],
                        }
                    )

        # Apply modifications by replacing lines
        if modifications:
            lines = source_code.splitlines()

            # Sort modifications by line number in reverse order to avoid offset issues
            modifications.sort(key=lambda x: x["lineno"], reverse=True)

            for mod in modifications:
                line_idx = mod["lineno"] - 1  # Convert to 0-based indexing
                if line_idx < len(lines):
                    original_line = lines[line_idx]

                    # Create the new import statement
                    if mod["names"]:
                        names_str = ", ".join(mod["names"])
                        if mod["absolute_module"]:
                            new_line = f"from {mod['absolute_module']} import {names_str}"
                        else:
                            # If absolute module is empty, convert to regular import
                            new_line = f"import {names_str}"
                    else:
                        if mod["absolute_module"]:
                            new_line = f"import {mod['absolute_module']}"
                        else:
                            # Skip empty imports
                            continue

                    # Preserve indentation from original line
                    original_indent = len(original_line) - len(original_line.lstrip())
                    new_line = " " * original_indent + new_line

                    lines[line_idx] = new_line

            return "\n".join(lines)

        return source_code

    def _get_all_file_contents(self) -> dict:
        """
        Get a dictionary mapping relative file paths to their source code
        for all sibling and child files of the reward function.
        Converts relative imports to absolute imports in the process.

        Returns:
            Dictionary with relative paths as keys and source code as values
        """
        file_contents = {}

        # Get all sibling and child files
        all_files = self._get_sibling_and_child_files()

        for file_path in all_files:
            relative_path = self._get_relative_path(file_path)
            source_code = self._get_file_source(file_path)
            # Convert relative imports to absolute imports
            converted_source = self._convert_relative_imports(source_code, file_path)
            file_contents[relative_path] = converted_source

        return file_contents

    def _create_evaluator_proto(self) -> SyncEvaluator:
        """Create the SyncEvaluator proto object from the reward function"""
        requirements = self._reward_function._reward_function_requirements

        # get dependencies
        if not requirements:
            file_path = inspect.getsourcefile(self._reward_function)
            dependencies_file_path = find_requirements_or_pyproject(file_path)
            requirements = get_requirements_from_pyproject_or_requirements_txt(dependencies_file_path)

        code_snippets = SyncCodeSnippets(
            file_contents=self._get_all_file_contents(),
            language="python",
            entry_file=self._reward_function_relative_path,
            entry_func=self._reward_function_name,
        )

        criteria = [
            SyncCriterion(
                name=self._reward_function.__name__,
                code_snippets=code_snippets,
                type=SyncCriterion.Type.CODE_SNIPPETS,
            )
        ]

        evaluator = SyncEvaluator(
            criteria=criteria,
            requirements=requirements,
            multi_metrics=True,
            rollup_settings=SyncRollupSettings(
                skip_rollup=True,
            ),
        )

        if self._reward_function.__doc__:
            evaluator.description = self._reward_function.__doc__.strip()

        return evaluator

    @property
    def name_prefix(self) -> str:
        """Get the name prefix of the evaluator"""
        id = self._reward_function._reward_function_id
        if not id:
            raise ValueError("Reward function must have an ID")
        return id

    def _list_existing_evaluators(self) -> List[SyncEvaluator]:
        """List all existing evaluators and filter by name prefix"""
        # Paginate through all evaluators
        all_evaluators: List[SyncEvaluator] = []
        page_token = None

        while True:
            list_evaluators_request = SyncListEvaluatorsRequest(
                page_size=200,
                page_token=page_token,
            )
            response = self._gateway.list_evaluators_sync(list_evaluators_request)

            all_evaluators.extend(response.evaluators)

            # Check if there are more pages
            if not response.next_page_token:
                break
            page_token = response.next_page_token

        # filter evaluators that start with name prefix, accounting for full paths
        evaluators = [
            evaluator for evaluator in all_evaluators if evaluator.name.split("/")[-1].startswith(self.name_prefix)
        ]

        return evaluators

    def _is_criterion_same(self, a: SyncCriterion, b: SyncCriterion) -> bool:
        """Compare two criteria for equality"""
        # recursively compare code_snippets
        if a.code_snippets.file_contents != b.code_snippets.file_contents:
            return False
        return True

    def _is_evaluator_same(self, a: SyncEvaluator, b: SyncEvaluator) -> bool:
        """Compare two evaluators for equality"""
        # recursively compare criteria
        if len(a.criteria) != len(b.criteria):
            return False
        if a.requirements != b.requirements:
            return False
        for a_criterion, b_criterion in zip(a.criteria, b.criteria):
            if not self._is_criterion_same(a_criterion, b_criterion):
                return False
        return True

    def preview(self, dataset) -> SyncPreviewEvaluatorResponse:
        sample_data = [json.dumps(j) for j in dataset]
        self.sync()
        if not self._proto:
            raise ValueError("Evaluator not synced. Something went wrong with the sync.")
        response = self._gateway.preview_evaluator_sync(
            SyncPreviewEvaluatorRequest(evaluator=self._proto, sample_data=sample_data)
        )
        return response

    def _extract_version_number(self, evaluator_name: str) -> int:
        """
        Extract the version number from an evaluator name.
        Returns 0 if no version is found.

        Args:
            evaluator_name: The full evaluator name

        Returns:
            The version number as an integer
        """
        evaluator_id = evaluator_name.split("/")[-1]

        if self.VERSION_DELIMITER in evaluator_id:
            try:
                version_str = evaluator_id.split(self.VERSION_DELIMITER)[-1]
                return int(version_str)
            except (ValueError, IndexError):
                return 0
        return 0

    def sync(self) -> "Evaluator":
        """
        Create or retrieve the evaluator on Fireworks.
        If an identical evaluator exists, reuse it. Otherwise, create a new versioned evaluator.
        """
        if self._proto is not None:
            logger.debug(f"Evaluator already synced: {self._proto.name}")
            return self

        # Create the evaluator proto
        evaluator_proto = self._create_evaluator_proto()

        # Get existing evaluators with matching name prefix
        existing_evaluators = self._list_existing_evaluators()

        # Check all existing evaluators for a match
        matching_evaluator = None
        for evaluator in existing_evaluators:
            if self._is_evaluator_same(evaluator, evaluator_proto):
                matching_evaluator = evaluator
                break

        if matching_evaluator:
            logger.debug(f"Using existing evaluator: {matching_evaluator.name}")
            self._proto = matching_evaluator
        else:
            # Find the latest version number to increment
            latest_version = 0
            for evaluator in existing_evaluators:
                version = self._extract_version_number(evaluator.name)
                latest_version = max(latest_version, version)

            # Create a new evaluator with incremented version
            evaluator_id = f"{self.name_prefix}{self.VERSION_DELIMITER}{latest_version + 1}"
            evaluator_proto.display_name = evaluator_id

            create_evaluator_request = SyncCreateEvaluatorRequest(
                evaluator=evaluator_proto,
                evaluator_id=evaluator_id,
            )

            logger.debug(f"Creating new evaluator: {evaluator_id}")
            self._proto = self._gateway.create_evaluator_sync(create_evaluator_request)

        return self

    @property
    def name(self) -> str:
        """Get the name of the evaluator"""
        if not self._proto:
            raise ValueError("Evaluator has no name. Make sure to run `sync` before calling this method.")
        return self._proto.name

    @property
    def id(self) -> str:
        """Get the ID of the evaluator"""
        if not self._proto:
            raise ValueError("Evaluator has no ID. Make sure to run `sync` before calling this method.")
        return self._proto.name.split("/")[-1]

    @property
    def url(self) -> str:
        """Get the URL to view this evaluator in the Fireworks dashboard"""
        return f"https://app.fireworks.ai/dashboard/evaluators/{self.id}"
