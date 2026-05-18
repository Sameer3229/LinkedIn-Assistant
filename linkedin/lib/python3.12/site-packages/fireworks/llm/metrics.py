from collections import defaultdict, deque
from typing import Optional


class Metrics:
    """
    A class for tracking and analyzing performance metrics for LLM operations.

    This class maintains a rolling window of metrics such as response times,
    token generation speeds, and other performance indicators. It provides
    statistical methods to analyze these metrics (mean, median, min, max).

    Each metric is stored as a list of values with a maximum size to prevent
    unbounded memory growth. When the maximum size is reached, the oldest
    values are removed in a FIFO manner.
    """

    def __init__(self, max_metrics: int = 1000):
        """
        Initialize the metrics tracker.

        Args:
            max_metrics: Maximum number of values to store for each metric.
                         Defaults to 1000. When exceeded, oldest values are removed.
        """
        self._metrics = defaultdict(deque)
        self._max_metrics = max_metrics

    def add_metric(self, metric_name: str, metric_value: float):
        """
        Add a new metric value to the specified metric.

        Args:
            metric_name: Name of the metric to track
            metric_value: Value to add to the metric
        """
        self._metrics[metric_name].append(metric_value)
        if len(self._metrics[metric_name]) > self._max_metrics:
            self._metrics[metric_name].popleft()

    def get_metric(self, metric_name: str):
        """
        Get all recorded values for a specific metric.

        Args:
            metric_name: Name of the metric to retrieve

        Returns:
            List of metric values or None if the metric doesn't exist
        """
        if metric_name not in self._metrics:
            return None
        return self._metrics[metric_name]

    def get_metric_mean(self, metric_name: str) -> Optional[float]:
        """
        Calculate the arithmetic mean of a metric's values.

        Args:
            metric_name: Name of the metric

        Returns:
            Mean value or None if the metric doesn't exist
        """
        if metric_name not in self._metrics:
            return None
        return sum(self._metrics[metric_name]) / len(self._metrics[metric_name])

    def get_metric_median(self, metric_name: str):
        """
        Calculate the median value of a metric.

        Args:
            metric_name: Name of the metric

        Returns:
            Median value or None if the metric doesn't exist
        """
        if metric_name not in self._metrics:
            return None
        return sorted(self._metrics[metric_name])[len(self._metrics[metric_name]) // 2]

    def get_metric_min(self, metric_name: str):
        """
        Get the minimum value recorded for a metric.

        Args:
            metric_name: Name of the metric

        Returns:
            Minimum value or None if the metric doesn't exist
        """
        if metric_name not in self._metrics:
            return None
        return min(self._metrics[metric_name])

    def get_metric_max(self, metric_name: str):
        """
        Get the maximum value recorded for a metric.

        Args:
            metric_name: Name of the metric

        Returns:
            Maximum value or None if the metric doesn't exist
        """
        if metric_name not in self._metrics:
            return None
        return max(self._metrics[metric_name])
