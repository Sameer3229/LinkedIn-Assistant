/**
 * Background Service Worker for LinkedIn Message Tracker
 * Handles message passing from content script and manages storage
 */

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "SAVE_CHAT_HISTORY") {
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
    
    // Return true to keep the message channel open for async response
    return true;
  }
});
