document.addEventListener("DOMContentLoaded", () => {
  const openAdminBtn = document.getElementById("openAdmin");

  openAdminBtn.addEventListener("click", () => {
    chrome.tabs.create({ url: chrome.runtime.getURL("admin/index.html") });
  });
});

