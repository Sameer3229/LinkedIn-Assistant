document.addEventListener("DOMContentLoaded", () => {
  const promptInput = document.getElementById("promptInput");
  const saveBtn = document.getElementById("saveBtn");
  const status = document.getElementById("status");

  const showStatus = () => {
    status.style.display = "block";

    setTimeout(() => {
      status.style.display = "none";
    }, 2000);
  };

  (async () => {
    try {
      const result = await chrome.storage.local.get(["systemPrompt"]);
      promptInput.value = result.systemPrompt || "";
    } catch (error) {
      console.warn("Prompt load failed:", error);
    }
  })();

  saveBtn.addEventListener("click", async () => {
    const trimmedPrompt = promptInput.value.trim();
    const payload = {
      systemPrompt: trimmedPrompt,
      systemPromptVersion: String(Date.now()),
    };

    try {
      await chrome.storage.local.set(payload);
      showStatus();
    } catch (error) {
      console.error("Prompt save failed:", error);
    }
  });
});
