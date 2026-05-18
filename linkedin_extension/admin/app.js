// ========================================
// Admin Portal Application Logic
// ========================================

const API_BASE = "https://linkedinassitantapi.hnhsofttechsolutions.com";
// const API_BASE = "http://localhost:9011";
let currentToken = null;
let currentUsername = null;
let currentEditingPromptId = null;

// Initialize on page load
window.addEventListener("DOMContentLoaded", () => {
  initializePortal();
});

// Initialize portal
function initializePortal() {
  chrome.storage.local.get(["auth_token", "username"], async (result) => {
    currentToken = result.auth_token || null;
    currentUsername = result.username || null;

    if (!currentToken || !currentUsername) {
      window.location.href = "./auth.html";
      return;
    }

    try {
      const response = await fetch(`${API_BASE}/admin/auth/verify`, {
        headers: { "Authorization": `Bearer ${currentToken}` }
      });
      if (!response.ok) {
        chrome.storage.local.remove(["auth_token", "username", "user_id"]);
        window.location.href = "./auth.html";
        return;
      }
    } catch (err) {
      console.error("Auth verification failed:", err);
      window.location.href = "./auth.html";
      return;
    }

    document.getElementById("currentUser").textContent = currentUsername;

    // Static button listeners (no inline onclick — blocked by extension CSP)
    document.getElementById("logoutBtn").addEventListener("click", handleLogout);
    document.getElementById("savePromptBtn").addEventListener("click", handleSavePrompt);
    document.getElementById("cancelEditBtn").addEventListener("click", resetPromptForm);
    document.getElementById("clearHistoryBtn").addEventListener("click", clearHistory);

    // Tab buttons
    document.getElementById("tab-prompts").addEventListener("click", () => switchTab("prompts"));
    document.getElementById("tab-documents").addEventListener("click", () => switchTab("documents"));
    document.getElementById("tab-history").addEventListener("click", () => switchTab("history"));

    // Event delegation for prompt table action buttons
    document.getElementById("promptsTableBody").addEventListener("click", (e) => {
      const btn = e.target.closest("button[data-prompt-id]");
      if (!btn) return;
      const id = parseInt(btn.dataset.promptId, 10);
      if (btn.classList.contains("edit-btn")) editPrompt(id);
      else if (btn.classList.contains("delete-btn")) deletePrompt(id);
      else if (btn.classList.contains("default-btn")) setDefault(id);
    });

    // Document tab listeners
    const dropZone = document.getElementById("uploadDropZone");
    const fileInput = document.getElementById("docFileInput");

    dropZone.addEventListener("click", () => fileInput.click());
    dropZone.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropZone.classList.add("dragover");
    });
    dropZone.addEventListener("dragleave", () => dropZone.classList.remove("dragover"));
    dropZone.addEventListener("drop", (e) => {
      e.preventDefault();
      dropZone.classList.remove("dragover");
      if (e.dataTransfer.files.length) {
        fileInput.files = e.dataTransfer.files;
        showUploadFileNames(e.dataTransfer.files);
      }
    });
    fileInput.addEventListener("change", () => showUploadFileNames(fileInput.files));

    document.getElementById("uploadFilesBtn").addEventListener("click", handleFileUpload);
    document.getElementById("addUrlBtn").addEventListener("click", handleUrlAdd);
    document.getElementById("refreshDocsBtn").addEventListener("click", loadDocuments);

    // Event delegation for document table actions (delete + toggle)
    document.getElementById("documentsTableBody").addEventListener("click", (e) => {
      const btn = e.target.closest("button[data-doc-id]");
      if (!btn) return;
      const id = parseInt(btn.dataset.docId, 10);
      deleteDocument(id);
    });

    document.getElementById("documentsTableBody").addEventListener("change", (e) => {
      const chk = e.target.closest("input.doc-toggle[data-doc-id]");
      if (!chk) return;
      const id = parseInt(chk.dataset.docId, 10);
      toggleDocument(id);
    });

    loadPrompts();
  });
}

// ========================================
// Tab Management
// ========================================

function switchTab(tabName) {
  document.querySelectorAll(".tab-content").forEach(tab => tab.classList.remove("active"));
  document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
  document.getElementById("panel-" + tabName).classList.add("active");
  document.getElementById("tab-" + tabName).classList.add("active");

  if (tabName === "history") loadHistory();
  if (tabName === "documents") loadDocuments();
}

// ========================================
// Prompt Manager Functions
// ========================================

async function loadPrompts() {
  try {
    const response = await fetch(`${API_BASE}/admin/prompts`, {
      headers: { "Authorization": `Bearer ${currentToken}` }
    });
    if (!response.ok) { showError("Failed to load prompts"); return; }

    const data = await response.json();
    const prompts = data.prompts || [];
    const tbody = document.querySelector("#promptsTableBody");
    tbody.innerHTML = "";

    if (prompts.length === 0) {
      tbody.innerHTML = '<tr><td colspan="5" style="text-align:center;color:#666;">No prompts yet. Create one to get started!</td></tr>';
      return;
    }

    prompts.forEach(prompt => {
      const row = document.createElement("tr");
      const createdDate = new Date(prompt.created_at).toLocaleDateString();
      const defaultBadge = prompt.is_default ? '<span class="badge-default">Default</span>' : '';

      if (prompt.is_default) {
        chrome.storage.local.set({ selected_prompt_id: prompt.id });
      }

      row.innerHTML = `
        <td>${escapeHtml(prompt.name)}</td>
        <td>${escapeHtml(prompt.description || "—")}</td>
        <td>${createdDate}</td>
        <td>${defaultBadge}</td>
        <td>
          <button class="action-btn edit-btn" data-prompt-id="${prompt.id}">Edit</button>
          <button class="action-btn delete-btn" data-prompt-id="${prompt.id}">Delete</button>
          ${!prompt.is_default ? `<button class="action-btn default-btn" data-prompt-id="${prompt.id}">Set Default</button>` : ''}
        </td>
      `;
      tbody.appendChild(row);
    });
  } catch (err) {
    showError("Error loading prompts: " + err.message);
  }
}

async function handleSavePrompt() {
  const name = document.getElementById("promptName").value.trim();
  const description = document.getElementById("promptDesc").value.trim();
  const content = document.getElementById("promptContent").value.trim();

  if (!name || !content) { showError("Prompt name and content are required"); return; }

  const saveBtn = document.getElementById("savePromptBtn");
  saveBtn.disabled = true;

  try {
    const url = currentEditingPromptId
      ? `${API_BASE}/admin/prompts/${currentEditingPromptId}`
      : `${API_BASE}/admin/prompts`;
    const method = currentEditingPromptId ? "PUT" : "POST";

    const response = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json", "Authorization": `Bearer ${currentToken}` },
      body: JSON.stringify({ name, description, content })
    });

    if (!response.ok) {
      const data = await response.json();
      showError(data.detail || "Failed to save prompt");
      saveBtn.disabled = false;
      return;
    }

    showSuccess(currentEditingPromptId ? "Prompt updated successfully" : "Prompt created successfully");
    clearForm();
    loadPrompts();
  } catch (err) {
    showError("Error saving prompt: " + err.message);
  }
  saveBtn.disabled = false;
}

function clearForm() {
  currentEditingPromptId = null;
  document.getElementById("promptForm").reset();
  document.getElementById("promptName").value = "";
  document.getElementById("promptDesc").value = "";
  document.getElementById("promptContent").value = "";
  document.getElementById("savePromptBtn").textContent = "Save Prompt";
  document.getElementById("cancelEditBtn").style.display = "none";
}

function editPrompt(promptId) {
  currentEditingPromptId = promptId;
  fetch(`${API_BASE}/admin/prompts`, { headers: { "Authorization": `Bearer ${currentToken}` } })
    .then(r => r.json())
    .then(data => {
      const prompt = data.prompts.find(p => p.id === promptId);
      if (prompt) {
        document.getElementById("promptName").value = prompt.name;
        document.getElementById("promptDesc").value = prompt.description || "";
        document.getElementById("promptContent").value = prompt.content;
        document.getElementById("savePromptBtn").textContent = "Update Prompt";
        document.getElementById("cancelEditBtn").style.display = "inline-block";
        document.getElementById("promptForm").scrollIntoView({ behavior: "smooth" });
        showSuccess("Loaded prompt for editing");
      } else {
        showError("Prompt not found");
      }
    })
    .catch(err => showError("Error loading prompt: " + err.message));
}

function resetPromptForm() { clearForm(); }

async function deletePrompt(promptId) {
  if (!confirm("Are you sure you want to delete this prompt?")) return;
  try {
    const response = await fetch(`${API_BASE}/admin/prompts/${promptId}`, {
      method: "DELETE",
      headers: { "Authorization": `Bearer ${currentToken}` }
    });
    if (!response.ok) { const d = await response.json(); showError(d.detail || "Failed to delete"); return; }
    showSuccess("Prompt deleted");
    loadPrompts();
  } catch (err) {
    showError("Error deleting prompt: " + err.message);
  }
}

async function setDefault(promptId) {
  try {
    const response = await fetch(`${API_BASE}/admin/prompts/${promptId}/set-default`, {
      method: "PUT",
      headers: { "Authorization": `Bearer ${currentToken}` }
    });
    if (!response.ok) { const d = await response.json(); showError(d.detail || "Failed to set default"); return; }
    chrome.storage.local.set({ selected_prompt_id: promptId });
    showSuccess("Default prompt updated");
    loadPrompts();
  } catch (err) {
    showError("Error setting default: " + err.message);
  }
}

// ========================================
// Document Management Functions (RAG)
// ========================================

function showUploadFileNames(files) {
  const status = document.getElementById("uploadStatus");
  if (!files || files.length === 0) { status.style.display = "none"; return; }
  const names = Array.from(files).map(f => f.name).join(", ");
  status.textContent = `Selected: ${names}`;
  status.className = "upload-status info";
  status.style.display = "block";
}

async function handleFileUpload() {
  const fileInput = document.getElementById("docFileInput");
  const status = document.getElementById("uploadStatus");

  if (!fileInput.files || fileInput.files.length === 0) {
    status.textContent = "Please select at least one file first.";
    status.className = "upload-status error";
    status.style.display = "block";
    return;
  }

  const uploadBtn = document.getElementById("uploadFilesBtn");
  uploadBtn.disabled = true;
  uploadBtn.textContent = "Uploading...";
  status.textContent = "Uploading and indexing files — this may take a moment...";
  status.className = "upload-status info";
  status.style.display = "block";

  const formData = new FormData();
  for (const file of fileInput.files) {
    formData.append("files", file);
  }

  try {
    const response = await fetch(`${API_BASE}/admin/documents/upload`, {
      method: "POST",
      headers: { "Authorization": `Bearer ${currentToken}` },
      body: formData
    });

    const data = await response.json();

    if (!response.ok) {
      status.textContent = data.detail || "Upload failed.";
      status.className = "upload-status error";
      return;
    }

    const results = data.results || [];
    const ok = results.filter(r => r.status === "ok");
    const errors = results.filter(r => r.status === "error");
    const skipped = results.filter(r => r.status === "skipped");

    let msg = "";
    if (ok.length) msg += `Indexed ${ok.length} file(s). `;
    if (errors.length) msg += `${errors.length} error(s): ${errors.map(e => e.filename + " — " + e.reason).join("; ")}. `;
    if (skipped.length) msg += `${skipped.length} skipped (unsupported type). `;

    status.textContent = msg.trim();
    status.className = errors.length ? "upload-status error" : "upload-status success";
    fileInput.value = "";
    loadDocuments();
  } catch (err) {
    status.textContent = "Connection error: " + err.message;
    status.className = "upload-status error";
  } finally {
    uploadBtn.disabled = false;
    uploadBtn.textContent = "Upload Files";
  }
}

async function handleUrlAdd() {
  const urlInput = document.getElementById("docUrlInput");
  const status = document.getElementById("urlStatus");
  const url = urlInput.value.trim();

  if (!url) {
    status.textContent = "Please enter a URL.";
    status.className = "upload-status error";
    status.style.display = "block";
    return;
  }

  const addBtn = document.getElementById("addUrlBtn");
  addBtn.disabled = true;
  addBtn.textContent = "Fetching...";
  status.textContent = "Fetching and indexing page content — this may take a moment...";
  status.className = "upload-status info";
  status.style.display = "block";

  try {
    const response = await fetch(`${API_BASE}/admin/documents/url`, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Authorization": `Bearer ${currentToken}` },
      body: JSON.stringify({ url })
    });

    const data = await response.json();

    if (!response.ok) {
      status.textContent = data.detail || "Failed to index URL.";
      status.className = "upload-status error";
      return;
    }

    status.textContent = `Indexed "${data.filename}" — ${data.chunks} chunk(s) created.`;
    status.className = "upload-status success";
    urlInput.value = "";
    loadDocuments();
  } catch (err) {
    status.textContent = "Connection error: " + err.message;
    status.className = "upload-status error";
  } finally {
    addBtn.disabled = false;
    addBtn.textContent = "Add URL";
  }
}

async function loadDocuments() {
  const tbody = document.getElementById("documentsTableBody");
  const emptyState = document.getElementById("emptyDocsState");
  const errorDiv = document.getElementById("docsError");
  tbody.innerHTML = "";
  emptyState.style.display = "none";
  errorDiv.style.display = "none";

  try {
    const response = await fetch(`${API_BASE}/admin/documents`, {
      headers: { "Authorization": `Bearer ${currentToken}` }
    });

    if (!response.ok) {
      errorDiv.textContent = "Failed to load documents.";
      errorDiv.style.display = "block";
      return;
    }

    const data = await response.json();
    const docs = data.documents || [];

    if (docs.length === 0) {
      emptyState.style.display = "block";
      return;
    }

    docs.forEach(doc => {
      const row = document.createElement("tr");
      const date = new Date(doc.created_at).toLocaleDateString();
      const label = doc.source_url
        ? `<a href="${escapeHtml(doc.source_url)}" target="_blank" rel="noopener" title="${escapeHtml(doc.source_url)}">${escapeHtml(doc.filename)}</a>`
        : escapeHtml(doc.filename);
      const isActive = doc.is_active === 1 || doc.is_active === true;

      row.innerHTML = `
        <td>${label}</td>
        <td><span class="doc-type-badge doc-type-${doc.doc_type}">${doc.doc_type.toUpperCase()}</span></td>
        <td>${doc.chunk_count}</td>
        <td>${date}</td>
        <td>
          <label class="toggle-switch" title="${isActive ? "Disable context" : "Enable context"}">
            <input type="checkbox" class="doc-toggle" data-doc-id="${doc.id}" ${isActive ? "checked" : ""}>
            <span class="toggle-slider"></span>
          </label>
        </td>
        <td><button class="action-btn delete-btn" data-doc-id="${doc.id}">Delete</button></td>
      `;
      tbody.appendChild(row);
    });
  } catch (err) {
    errorDiv.textContent = "Error loading documents: " + err.message;
    errorDiv.style.display = "block";
  }
}

async function deleteDocument(docId) {
  if (!confirm("Delete this document and remove its embeddings from the knowledge base?")) return;

  try {
    const response = await fetch(`${API_BASE}/admin/documents/${docId}`, {
      method: "DELETE",
      headers: { "Authorization": `Bearer ${currentToken}` }
    });

    if (!response.ok) {
      const data = await response.json();
      alert(data.detail || "Failed to delete document.");
      return;
    }

    loadDocuments();
  } catch (err) {
    alert("Error deleting document: " + err.message);
  }
}

async function toggleDocument(docId) {
  try {
    const response = await fetch(`${API_BASE}/admin/documents/${docId}/toggle`, {
      method: "PUT",
      headers: { "Authorization": `Bearer ${currentToken}` }
    });

    if (!response.ok) {
      const data = await response.json();
      alert(data.detail || "Failed to toggle document.");
      loadDocuments(); // revert checkbox state by reloading
    }
    // No full reload needed — the checkbox state already reflects the new value
  } catch (err) {
    alert("Error toggling document: " + err.message);
    loadDocuments(); // revert on error
  }
}

// ========================================
// Chat History Functions
// ========================================

async function loadHistory() {
  try {
    const response = await fetch(`${API_BASE}/admin/history`, {
      headers: { "Authorization": `Bearer ${currentToken}` }
    });
    if (!response.ok) { showError("Failed to load chat history"); return; }

    const data = await response.json();
    const history = data.history || [];
    const tbody = document.querySelector("#historyTableBody");
    tbody.innerHTML = "";

    if (history.length === 0) {
      tbody.innerHTML = '<tr><td colspan="4" style="text-align:center;color:#666;">No chat history yet</td></tr>';
      return;
    }

    history.forEach(entry => {
      const row = document.createElement("tr");
      const timestamp = new Date(entry.time).toLocaleString();
      const inbound = entry.inbound || "";
      const reply = entry.reply || "";
      const inboundPreview = escapeHtml(inbound).substring(0, 80) + (inbound.length > 80 ? "..." : "");
      const replyPreview = escapeHtml(reply).substring(0, 80) + (reply.length > 80 ? "..." : "");

      row.innerHTML = `
        <td>${timestamp}</td>
        <td>${escapeHtml(entry.name)}</td>
        <td><pre style="margin:0;font-size:12px;white-space:pre-wrap;">${inboundPreview}</pre></td>
        <td><pre style="margin:0;font-size:12px;white-space:pre-wrap;">${replyPreview}</pre></td>
      `;
      tbody.appendChild(row);
    });
  } catch (err) {
    showError("Error loading history: " + err.message);
  }
}

async function clearHistory() {
  if (!confirm("Clear all chat history? This cannot be undone.")) return;
  try {
    const response = await fetch(`${API_BASE}/admin/history`, {
      method: "DELETE",
      headers: { "Authorization": `Bearer ${currentToken}` }
    });
    if (!response.ok) { const d = await response.json(); showError(d.detail || "Failed to clear history"); return; }
    showSuccess("Chat history cleared");
    loadHistory();
  } catch (err) {
    showError("Error clearing history: " + err.message);
  }
}

// ========================================
// Logout
// ========================================

function handleLogout() {
  if (!confirm("Are you sure you want to logout?")) return;
  chrome.storage.local.remove(["auth_token", "user_id", "username", "selected_prompt_id"], () => {
    window.location.href = "./auth.html";
  });
}

// ========================================
// Utility Functions
// ========================================

function showError(message) {
  const messageDiv = document.getElementById("promptFormError");
  messageDiv.textContent = message;
  messageDiv.style.display = "block";
  setTimeout(() => { messageDiv.style.display = "none"; }, 5000);
}

function showSuccess(message) {
  const messageDiv = document.getElementById("promptFormSuccess");
  messageDiv.textContent = "✓ " + message;
  messageDiv.style.display = "block";
  setTimeout(() => { messageDiv.style.display = "none"; }, 3000);
}

function escapeHtml(text) {
  if (!text) return "";
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}
