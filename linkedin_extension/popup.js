document.addEventListener("DOMContentLoaded", () => {
  // Tab switching
  const tabs = { prompt: document.getElementById("tab-prompt"), history: document.getElementById("tab-history") };
  const panels = { prompt: document.getElementById("panel-prompt"), history: document.getElementById("panel-history") };

  Object.keys(tabs).forEach(key => {
    tabs[key].addEventListener("click", () => {
      Object.keys(tabs).forEach(k => { tabs[k].classList.remove("active"); panels[k].classList.remove("active"); });
      tabs[key].classList.add("active");
      panels[key].classList.add("active");
      if (key === "history") loadHistory();
    });
  });

  // Prompt Manager
  const promptInput = document.getElementById("promptInput");
  const saveBtn = document.getElementById("saveBtn");
  const status = document.getElementById("status");

  chrome.storage.local.get(["systemPrompt"], (result) => {
    promptInput.value = result.systemPrompt || "";
  });

  saveBtn.addEventListener("click", async () => {
    const trimmedPrompt = promptInput.value.trim();
    await chrome.storage.local.set({
      systemPrompt: trimmedPrompt,
      systemPromptVersion: String(Date.now()),
    });
    status.style.display = "block";
    setTimeout(() => { status.style.display = "none"; }, 2000);
  });

  // Chat History
  function loadHistory() {
    chrome.storage.local.get(["botChatHistory"], (result) => {
      const history = result.botChatHistory || [];
      const list = document.getElementById("chatList");

      if (history.length === 0) {
        list.innerHTML = '<div class="empty-state">No conversations replied to yet.</div>';
        return;
      }

      // Show newest first
      const sorted = [...history].reverse();
      list.innerHTML = sorted.map(entry => `
        <div class="chat-card">
          <div class="avatar">${entry.name ? entry.name[0].toUpperCase() : "?"}</div>
          <div class="chat-meta">
            <span class="chat-name">${entry.name || "Unknown"}</span>
            <span class="chat-time">${entry.time || ""}</span>
            <div class="chat-preview">${escapeHtml(entry.inbound || "")}</div>
            <div><span class="reply-label">Bot replied: </span><span class="chat-reply">${escapeHtml(entry.reply || "")}</span></div>
          </div>
        </div>
      `).join("");
    });
  }

  document.getElementById("clearHistory").addEventListener("click", () => {
    chrome.storage.local.set({ botChatHistory: [] }, () => {
      loadHistory();
    });
  });

  function escapeHtml(str) {
    return String(str).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
  }
});

