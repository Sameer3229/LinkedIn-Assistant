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
            // Wait for messaging page to load, then collect names and process
            setTimeout(collectAndProcess, 3000);
        }
    }
}

// === STEP 1: Collect ALL unread chat NAMES first (before LinkedIn clears indicators) ===
function collectAndProcess() {
    if (isProcessing) return;
    isProcessing = true;

    const allCards = document.querySelectorAll('.msg-conversation-card__content--selectable');
    const unreadNames = [];

    allCards.forEach(card => {
        const hasUnreadSnippet = card.querySelector('.msg-conversation-card__message-snippet--unread') !== null;
        const hasUnreadBadge = card.querySelector('.msg-conversation-card__unread-count') !== null;
        const nameEl = card.querySelector('h3.msg-conversation-card__participant-names');
        const isBoldName = nameEl?.classList?.contains('t-bold');

        if (hasUnreadSnippet || hasUnreadBadge || isBoldName) {
            const name = nameEl?.innerText?.trim() || "";
            if (name && !repliedChats.has(name) && !unreadNames.includes(name)) {
                unreadNames.push(name);
                console.log(`%c[FOUND] Unread: ${name}`, "background:#f59e0b;color:black;padding:2px 6px;");
            }
        }
    });

    if (unreadNames.length === 0) {
        console.log("%c[INFO] No unread chats to reply.", "background:#6b7280;color:white;padding:2px 6px;");
        isProcessing = false;
        return;
    }

    console.log(`%c[QUEUE] ${unreadNames.length} unread chat(s) to process: ${unreadNames.join(', ')}`, "background:#8b5cf6;color:white;padding:2px 6px;font-weight:bold;");

    // Start processing by name, one by one
    processByName(unreadNames, 0);
}

// === STEP 2: Find card by NAME (fresh DOM lookup each time), click it, reply ===
function processByName(names, index) {
    if (index >= names.length) {
        console.log(`%c[DONE] All ${names.length} unread chats replied! Refreshing page...`, "background:#059669;color:white;padding:2px 6px;font-weight:bold;");
        isProcessing = false;
        window.lastCount = null;

        // Refresh page after all replies sent
        setTimeout(() => {
            console.log("%c[REFRESH] Reloading page...", "background:#2563eb;color:white;padding:2px 6px;font-weight:bold;");
            window.location.reload();
        }, 3000);
        return;
    }

    const targetName = names[index];
    console.log(`%c[PROCESSING ${index + 1}/${names.length}] ${targetName}`, "background:#f59e0b;color:black;padding:2px 6px;font-weight:bold;");

    // Fresh DOM search: find the conversation card by matching the name text
    const card = findCardByName(targetName);

    if (!card) {
        console.log(`⚠️ Card not found for "${targetName}". Skipping...`);
        repliedChats.add(targetName);
        setTimeout(() => processByName(names, index + 1), 1000);
        return;
    }

    // Click the card to open the conversation
    card.click();

    // Wait for input box to appear (chat loaded)
    waitForElement('.msg-form__contenteditable[role="textbox"]', 5000, (inputBox) => {
        if (!inputBox) {
            console.log(`❌ Input box not found for ${targetName}. Skipping...`);
            repliedChats.add(targetName);
            setTimeout(() => processByName(names, index + 1), 2000);
            return;
        }

        // Let LinkedIn fully settle
        setTimeout(() => {
            sendAutoReply("Hello, thanks for reaching out. I'm currently away, will get back to you soon!", (success) => {
                repliedChats.add(targetName);
                if (success) {
                    console.log(`%c[REPLIED ${index + 1}/${names.length}] ${targetName} ✅`, "background:#059669;color:white;padding:2px 6px;font-weight:bold;");
                } else {
                    console.log(`%c[FAILED ${index + 1}/${names.length}] ${targetName} ❌`, "background:#dc2626;color:white;padding:2px 6px;font-weight:bold;");
                }

                // Wait for LinkedIn to update, then process next name
                setTimeout(() => processByName(names, index + 1), 3000);
            });
        }, 1500);
    });
}

// === HELPER: Find conversation card by matching name text ===
function findCardByName(targetName) {
    const allCards = document.querySelectorAll('.msg-conversation-card__content--selectable');
    
    for (let i = 0; i < allCards.length; i++) {
        const nameEl = allCards[i].querySelector('h3.msg-conversation-card__participant-names');
        const name = nameEl?.innerText?.trim() || "";
        
        if (name === targetName) {
            return allCards[i];
        }
    }

    // Fallback: partial match (in case of extra spaces or slight differences)
    for (let i = 0; i < allCards.length; i++) {
        const nameEl = allCards[i].querySelector('h3.msg-conversation-card__participant-names');
        const name = nameEl?.innerText?.trim() || "";
        
        if (name.includes(targetName) || targetName.includes(name)) {
            return allCards[i];
        }
    }

    return null;
}

// === HELPER: Wait for element to appear in DOM ===
function waitForElement(selector, timeout, callback) {
    const startTime = Date.now();

    function check() {
        const el = document.querySelector(selector);
        if (el) {
            callback(el);
        } else if (Date.now() - startTime < timeout) {
            setTimeout(check, 300);
        } else {
            callback(null);
        }
    }

    check();
}

// === AUTO-REPLY LOGIC ===
function sendAutoReply(replyText, callback) {
    const inputBox = document.querySelector('.msg-form__contenteditable[role="textbox"]');
    if (!inputBox) {
        console.log("❌ Input box not found!");
        if (callback) callback(false);
        return;
    }

    // Clear, focus, and type
    inputBox.focus();
    inputBox.innerHTML = `<p>${replyText}</p>`;
    inputBox.dispatchEvent(new Event('input', { bubbles: true }));

    // Wait for send button to become enabled
    waitForSendButton(3000, (sendBtn) => {
        if (sendBtn) {
            sendBtn.click();
            console.log("%c[SENT] Reply Delivered", "background:#3b82f6;color:white;padding:2px 6px;");
            if (callback) setTimeout(() => callback(true), 1500);
        } else {
            // Retry: re-type and try again
            console.log("⚠️ Send button not enabled. Retrying...");
            inputBox.focus();
            inputBox.innerHTML = "";
            setTimeout(() => {
                inputBox.innerHTML = `<p>${replyText}</p>`;
                inputBox.dispatchEvent(new Event('input', { bubbles: true }));
                
                waitForSendButton(3000, (retryBtn) => {
                    if (retryBtn) {
                        retryBtn.click();
                        console.log("%c[SENT] Reply Delivered (retry)", "background:#3b82f6;color:white;padding:2px 6px;");
                        if (callback) setTimeout(() => callback(true), 1500);
                    } else {
                        console.log("❌ Send button still disabled after retry.");
                        if (callback) callback(false);
                    }
                });
            }, 500);
        }
    });
}

// === HELPER: Wait for send button to become enabled ===
function waitForSendButton(timeout, callback) {
    const startTime = Date.now();

    function check() {
        const btn = document.querySelector('.msg-form__send-button');
        if (btn && !btn.disabled) {
            callback(btn);
        } else if (Date.now() - startTime < timeout) {
            setTimeout(check, 300);
        } else {
            callback(null);
        }
    }

    check();
}

setInterval(finalScraper, 3000);