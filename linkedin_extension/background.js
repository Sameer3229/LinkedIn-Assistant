/**
 * Background Service Worker for LinkedIn Message Tracker
 * Handles message passing from content script and manages storage
 */
const API_BASE = "https://linkedinassitantapi.hnhsofttechsolutions.com";
// const API_BASE = "http://localhost:9011";

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "SAVE_CHAT_HISTORY") {
    // Save to local storage (for backwards compatibility)
    chrome.storage.local.get(["botChatHistory"], (result) => {
      const history = result.botChatHistory || [];
      
      // Keep only last 100 entries to avoid storage bloat
      if (history.length >= 100) {
        history.shift();
      }
      
      history.push(message.payload);
      chrome.storage.local.set({ botChatHistory: history }, () => {
        sendResponse({ success: true });
      });
    });

    // Also try to save to backend API
    // Use chrome.storage instead of localStorage (Manifest V3 compatibility)
    chrome.storage.local.get(["auth_token"], (result) => {
      const authToken = result.auth_token;
      if (authToken) {
        fetch("https://linkedinassitantapi.hnhsofttechsolutions.com/admin/history", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${authToken}`
          },
          body: JSON.stringify({
            name: message.payload.name || "Unknown",
            inbound: message.payload.inbound || "",
            reply: message.payload.reply || "",
            time: message.payload.time || new Date().toISOString()
          })
        }).catch(err => console.log("Could not save to backend:", err));
      }
    });
    
    // Return true to keep the message channel open for async response
    return true;
  }
});
