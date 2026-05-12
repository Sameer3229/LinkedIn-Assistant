console.log("LinkedIn Tracker: Global Monitoring Active...");

// 1. Error Filter
console.error = (function (_error) {
    return function (message) {
        if (typeof message === "string" && (message.includes("chrome-extension") || message.includes("invalid"))) return;
        _error.apply(console, arguments);
    };
})(console.error);

// Track replied conversations to avoid duplicate replies
const repliedChats = new Set();
let isProcessing = false;

function finalScraper() {
    // Don't start new scan if already handling chats
    if (isProcessing) return;

    const msgLink = document.querySelector('a[href*="/messaging/"]');

    // Only match VISIBLE badge (notification-badge--show), not the hidden empty one
    const badge = msgLink?.querySelector('.notification-badge--show');
    const badgeCount = badge?.querySelector('.notification-badge__count')?.innerText?.trim();

    // Also check aria-label for notification (fallback)
    const ariaLabel = msgLink?.getAttribute('aria-label') || "";
    const hasAriaNotification = ariaLabel.includes('new notification');

    // Only trigger if badge is visible with a count OR aria-label says there's a notification
    const hasNotification = (badge && badgeCount && badgeCount !== "0") || hasAriaNotification;

    if (hasNotification) {
        const count = badgeCount || ariaLabel.match(/(\d+)\s*new/)?.[1] || "?";
        if (window.lastCount !== count) {
            window.lastCount = count;
            console.log(`%c[!] NOTIFICATION: ${count}`, "background:#e11d48;color:white;padding:2px 6px;font-weight:bold;");
            msgLink.click();
            setTimeout(processUnreadChats, 3000);
        }
    }
}

function processUnreadChats() {
    if (isProcessing) return;
    isProcessing = true;

    // Find ALL conversation cards in the list
    const allCards = document.querySelectorAll('.msg-conversation-card__content--selectable');
    const unreadQueue = [];

    allCards.forEach(card => {
        // --- UNREAD DETECTION using exact LinkedIn classes ---
        // 1. Snippet has "msg-conversation-card__message-snippet--unread" class
        const hasUnreadSnippet = card.querySelector('.msg-conversation-card__message-snippet--unread') !== null;
        // 2. Unread count badge exists
        const hasUnreadBadge = card.querySelector('.msg-conversation-card__unread-count') !== null;
        // 3. Name h3 has t-bold (unread = bold, read = t-normal)
        const nameEl = card.querySelector('h3.msg-conversation-card__participant-names');
        const isBoldName = nameEl?.classList?.contains('t-bold');

        if (hasUnreadSnippet || hasUnreadBadge || isBoldName) {
            const name = nameEl?.innerText?.trim() || "Unknown";
            const snippet = card.querySelector('.msg-conversation-card__message-snippet')?.innerText?.trim() || "";

            // Skip if already replied to this person in this session
            if (repliedChats.has(name)) return;

            unreadQueue.push({ element: card, name, snippet });
            console.log(`%c[FOUND] Unread chat: ${name} — "${snippet}"`, "background:#f59e0b;color:black;padding:2px 6px;");
        }
    });

    if (unreadQueue.length === 0) {
        console.log("%c[INFO] No unread chats to reply.", "background:#6b7280;color:white;padding:2px 6px;");
        isProcessing = false;
        return;
    }

    console.log(`%c[QUEUE] ${unreadQueue.length} unread chat(s) to process`, "background:#8b5cf6;color:white;padding:2px 6px;font-weight:bold;");

    // Process them one by one (sequential)
    processNextChat(unreadQueue, 0);
}

function processNextChat(queue, index) {
    if (index >= queue.length) {
        console.log("%c[DONE] All unread chats processed!", "background:#059669;color:white;padding:2px 6px;font-weight:bold;");
        isProcessing = false;
        window.lastCount = null; // Reset so it re-checks on next interval
        return;
    }

    const chat = queue[index];
    console.log(`%c[PROCESSING ${index + 1}/${queue.length}] ${chat.name}`, "background:#f59e0b;color:black;padding:2px 6px;font-weight:bold;");
    console.log(`💬 Msg: ${chat.snippet}`);

    // Click on the conversation card to open it
    chat.element.click();

    // Wait for chat to load, then send reply
    setTimeout(() => {
        sendAutoReply("Hello, thanks for reaching out. I'm currently away, will get back to you soon!", (success) => {
            if (success) {
                repliedChats.add(chat.name);
                console.log(`%c[REPLIED ${index + 1}/${queue.length}] ${chat.name} ✅`, "background:#059669;color:white;padding:2px 6px;font-weight:bold;");
            } else {
                console.log(`%c[FAILED ${index + 1}/${queue.length}] ${chat.name} ❌`, "background:#dc2626;color:white;padding:2px 6px;font-weight:bold;");
            }
            // Move to next chat after delay
            setTimeout(() => processNextChat(queue, index + 1), 2000);
        });
    }, 2500);
}

// Auto-Reply Logic
function sendAutoReply(replyText, callback) {
    const inputBox = document.querySelector('.msg-form__contenteditable[role="textbox"]');
    if (!inputBox) {
        console.log("❌ Input box not found!");
        if (callback) callback(false);
        return;
    }

    inputBox.focus();
    inputBox.innerHTML = `<p>${replyText}</p>`;
    inputBox.dispatchEvent(new Event('input', { bubbles: true }));

    setTimeout(() => {
        const sendBtn = document.querySelector('.msg-form__send-button');
        if (sendBtn && !sendBtn.disabled) {
            sendBtn.click();
            console.log("%c[SENT] Reply Delivered", "background:#3b82f6;color:white;padding:2px 6px;");
            if (callback) setTimeout(() => callback(true), 1000);
        } else {
            // Retry once — sometimes LinkedIn needs a moment to enable the button
            console.log("⚠️ Send button disabled. Retrying...");
            setTimeout(() => {
                inputBox.focus();
                inputBox.innerHTML = `<p>${replyText}</p>`;
                inputBox.dispatchEvent(new Event('input', { bubbles: true }));
                setTimeout(() => {
                    const retryBtn = document.querySelector('.msg-form__send-button');
                    if (retryBtn && !retryBtn.disabled) {
                        retryBtn.click();
                        console.log("%c[SENT] Reply Delivered (retry)", "background:#3b82f6;color:white;padding:2px 6px;");
                        if (callback) setTimeout(() => callback(true), 1000);
                    } else {
                        console.log("❌ Send button still disabled.");
                        if (callback) callback(false);
                    }
                }, 1000);
            }, 500);
        }
    }, 1000);
}

setInterval(finalScraper, 3000);