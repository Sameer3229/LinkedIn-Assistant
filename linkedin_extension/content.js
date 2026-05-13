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
let pendingApiRequests = 0;
const CHAT_API_ENDPOINTS = [
    "http://localhost:8000/chat",
];
const MESSAGE_CARD_SELECTOR = ".msg-conversation-card__content--selectable";
const COMPOSER_SELECTOR = ".msg-form__contenteditable[role=\"textbox\"]";
const SEND_BUTTON_SELECTOR = ".msg-form__send-button";
const INBOX_READY_RETRY_LIMIT = 3;
const INBOX_READY_RETRY_DELAY_MS = 1000;
const COMPOSER_RETRY_LIMIT = 3;
const ACTIVE_THREAD_RETRY_LIMIT = 3;
const ACTIVE_THREAD_RETRY_DELAY_MS = 350;
const SEND_CONFIRMATION_TIMEOUT_MS = 4000;
const API_TIMEOUT_MS = 45000;
const API_RETRY_LIMIT = 2;
const API_RETRY_BASE_DELAY_MS = 1200;
const HUMAN_REPLY_DELAY_MS = [900, 1800];
const HUMAN_SEND_DELAY_MS = [600, 1400];
const HUMAN_REFRESH_DELAY_MS = [6000, 12000];
const HUMAN_TYPING_DELAY_MS = [18, 45];
const COMPOSER_FOCUS_DELAY_MS = 120;
const HEARTBEAT_INTERVAL_MS = 60000;
let lastHeartbeatAt = 0;
const REFRESH_IDLE_POLL_MS = 1500;

function logStage(stage, message) {
    console.log(`%c[${stage}] ${message}`, "background:#334155;color:white;padding:2px 6px;font-weight:bold;");
}

function randomBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function delay(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

async function humanPause(rangeMs) {
    const [min, max] = rangeMs;
    await delay(randomBetween(min, max));
}

function textMatchesTarget(text, targetName) {
    const normalizedText = cleanText(text).toLowerCase();
    const normalizedTarget = cleanText(targetName).toLowerCase();

    if (!normalizedText || !normalizedTarget) return false;

    return normalizedText.includes(normalizedTarget) || normalizedTarget.includes(normalizedText);
}

function getActiveThreadLabel() {
    const candidateSelectors = [
        '.msg-thread__participant-names',
        '.msg-thread__header h2',
        '.msg-thread__header h1',
        '.msg-thread__title',
    ];

    for (const selector of candidateSelectors) {
        const node = document.querySelector(selector);
        const label = cleanText(node?.innerText || node?.textContent);
        if (label) return label;
    }

    return cleanText(document.querySelector('.msg-thread')?.innerText || "");
}

function getActiveConversationName() {
    const activeCardSelectors = [
        '.msg-conversation-card--active',
        '.msg-conversation-card__content--selectable.active',
        '[aria-current="true"]',
        '.msg-conversation-listitem__link.active',
    ];

    for (const selector of activeCardSelectors) {
        const activeCard = document.querySelector(selector);
        const name = cleanText(activeCard?.querySelector('h3.msg-conversation-card__participant-names')?.innerText || "");
        if (name) return name;
    }

    return "";
}

function waitForActiveThread(targetName, timeout, callback) {
    const startTime = Date.now();

    function check() {
        const activeCardName = getActiveConversationName();
        const activeLabel = activeCardName || getActiveThreadLabel();

        if (textMatchesTarget(activeLabel, targetName)) {
            callback(true);
        } else if (Date.now() - startTime < timeout) {
            setTimeout(check, ACTIVE_THREAD_RETRY_DELAY_MS);
        } else {
            logStage("THREAD", `Thread mismatch for ${targetName}. Active label: "${activeLabel || "(empty)"}"`);
            callback(false);
        }
    }

    check();
}

function reopenConversation(targetName, callback) {
    const card = findCardByName(targetName);

    if (!card) {
        callback(false);
        return;
    }

    logStage("THREAD", `Reopening conversation for ${targetName}`);
    card.click();

    waitForActiveThread(targetName, 6000, (ready) => {
        if (!ready) {
            callback(false);
            return;
        }

        waitForElement(COMPOSER_SELECTOR, 6000, (inputBox) => {
            callback(Boolean(inputBox));
        });
    });
}

function finalScraper() {
    const now = Date.now();
    if (now - lastHeartbeatAt > HEARTBEAT_INTERVAL_MS) {
        lastHeartbeatAt = now;
        logStage("HEARTBEAT", "Scanner active.");
    }

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
            logStage("SCAN", `Notification detected: ${count}`);
            msgLink.click();
            waitForInboxReady(10000, (ready) => {
                if (!ready) {
                    logStage("WAIT", "Messaging inbox did not become ready in time; will retry on the next scan.");
                    window.lastCount = null;
                    return;
                }

                logStage("SCAN", "Messaging inbox is ready; collecting unread chats.");
                collectAndProcess();
            });
        }
    }
}

function scheduleRefreshAfterIdle() {
    const startTime = Date.now();

    function check() {
        if (pendingApiRequests === 0) {
            logStage("REFRESH", "Reloading page...");
            window.location.reload();
            return;
        }

        if (Date.now() - startTime > 60000) {
            logStage("REFRESH", "Pending API requests still active; skipping auto-refresh.");
            return;
        }

        setTimeout(check, REFRESH_IDLE_POLL_MS);
    }

    check();
}

// === STEP 1: Collect ALL unread chat NAMES first (before LinkedIn clears indicators) ===
function collectAndProcess(retryCount = 0) {
    if (isProcessing && retryCount === 0) return;
    if (!isProcessing) isProcessing = true;

    const allCards = document.querySelectorAll(MESSAGE_CARD_SELECTOR);
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

    if (allCards.length === 0 && retryCount < INBOX_READY_RETRY_LIMIT) {
        logStage("WAIT", `Conversation list not ready yet; retrying scan ${retryCount + 1}/${INBOX_READY_RETRY_LIMIT}`);
        setTimeout(() => collectAndProcess(retryCount + 1), INBOX_READY_RETRY_DELAY_MS);
        return;
    }

    if (unreadNames.length === 0) {
        if (retryCount < INBOX_READY_RETRY_LIMIT) {
            logStage("WAIT", `Unread markers not visible yet; rescanning ${retryCount + 1}/${INBOX_READY_RETRY_LIMIT}`);
            setTimeout(() => collectAndProcess(retryCount + 1), INBOX_READY_RETRY_DELAY_MS);
            return;
        }

        logStage("INFO", "No unread chats to reply.");
        isProcessing = false;
        return;
    }

    logStage("QUEUE", `${unreadNames.length} unread chat(s) to process: ${unreadNames.join(', ')}`);

    // Start processing by name, one by one
    processByName(unreadNames, 0);
}

// === STEP 2: Find card by NAME (fresh DOM lookup each time), click it, reply ===
function processByName(names, index) {
    if (index >= names.length) {
        logStage("DONE", `All ${names.length} unread chats processed. Refreshing page...`);
        isProcessing = false;
        window.lastCount = null;

        // Refresh page after all replies sent
        setTimeout(() => {
            scheduleRefreshAfterIdle();
        }, randomBetween(...HUMAN_REFRESH_DELAY_MS));
        return;
    }

    const targetName = names[index];
    logStage("PROCESS", `${index + 1}/${names.length} ${targetName}`);

    // Fresh DOM search: find the conversation card by matching the name text
    const card = findCardByName(targetName);

    if (!card) {
        logStage("WARN", `Card not found for "${targetName}". Continuing queue without marking replied.`);
        setTimeout(() => processByName(names, index + 1), 1000);
        return;
    }

    // Click the card to open the conversation
    card.click();

    // Wait for the correct thread to become active before typing.
    waitForActiveThread(targetName, 8000, (threadReady) => {
        if (!threadReady) {
            reopenConversation(targetName, (reopened) => {
                if (!reopened) {
                    logStage("WARN", `Thread did not confirm for ${targetName}. Will retry on a later scan.`);
                    setTimeout(() => processByName(names, index + 1), 2000);
                    return;
                }

                waitForElement(COMPOSER_SELECTOR, 8000, (inputBox) => {
                    if (!inputBox) {
                        logStage("WARN", `Input box not found after reopen for ${targetName}.`);
                        setTimeout(() => processByName(names, index + 1), 2000);
                        return;
                    }

                    setTimeout(() => {
                        sendDynamicReply(targetName, (success) => {
                            if (success) {
                                repliedChats.add(targetName);
                                logStage("SENT", `${index + 1}/${names.length} ${targetName}`);
                            } else {
                                logStage("FAILED", `${index + 1}/${names.length} ${targetName}`);
                            }

                            setTimeout(() => processByName(names, index + 1), 3000);
                        });
                    }, 1500);
                });
            });
            return;
        }

        // Wait for input box to appear (chat loaded)
        waitForElement(COMPOSER_SELECTOR, 8000, (inputBox) => {
        if (!inputBox) {
            logStage("WARN", `Input box not found for ${targetName}. Will retry on a later scan.`);
            setTimeout(() => processByName(names, index + 1), 2000);
            return;
        }

        // Let LinkedIn fully settle
        setTimeout(() => {
            sendDynamicReply(targetName, (success) => {
                if (success) {
                    repliedChats.add(targetName);
                    logStage("SENT", `${index + 1}/${names.length} ${targetName}`);
                } else {
                    logStage("FAILED", `${index + 1}/${names.length} ${targetName}`);
                }

                // Wait for LinkedIn to update, then process next name
                setTimeout(() => processByName(names, index + 1), 3000);
            });
        }, 1500);
    });
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

function waitForInboxReady(timeout, callback) {
    const startTime = Date.now();

    function check() {
        const cards = document.querySelectorAll(MESSAGE_CARD_SELECTOR);
        if (cards.length > 0) {
            callback(true);
        } else if (Date.now() - startTime < timeout) {
            setTimeout(check, 300);
        } else {
            callback(false);
        }
    }

    check();
}

function waitForComposerReady(timeout, callback) {
    const startTime = Date.now();

    function check() {
        const inputBox = document.querySelector(COMPOSER_SELECTOR);
        const sendButton = document.querySelector(SEND_BUTTON_SELECTOR);
        if (inputBox && sendButton) {
            callback(true);
        } else if (Date.now() - startTime < timeout) {
            setTimeout(check, 300);
        } else {
            callback(false);
        }
    }

    check();
}

function cleanText(text) {
    return typeof text === "string" ? text.replace(/\r\n/g, "\n").trim() : "";
}

function escapeHtml(text) {
    return cleanText(text)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

function formatReplyText(text) {
    return escapeHtml(text).replace(/\n/g, "<br>");
}

function extractConversationContext() {
    const candidateRoots = [
        document.querySelector('.msg-s-message-list'),
        document.querySelector('.msg-s-message-list-content'),
        document.querySelector('[class*="msg-s-message-list"]'),
    ].filter(Boolean);

    for (const root of candidateRoots) {
        const messages = [];
        const messageSelectors = [
            '.msg-s-message-group__message-text',
            '.msg-s-message-list__event',
            '.msg-s-event-listitem__body',
            '.msg-s-message-list__event p',
            '.msg-s-message-list__event span',
        ];

        for (const selector of messageSelectors) {
            const messageNodes = root.querySelectorAll(selector);
            messageNodes.forEach((node) => {
                const messageText = cleanText(node.innerText || node.textContent);
                if (messageText && !messages.includes(messageText)) {
                    messages.push(messageText);
                }
            });
        }

        if (messages.length > 0) {
            return messages.slice(-3).join("\n\n");
        }

        const fallbackText = cleanText(root.innerText || root.textContent);
        if (fallbackText) {
            return fallbackText.slice(-800);
        }
    }

    return "";
}

function buildReplyPrompt(targetName) {
    const conversationContext = extractConversationContext();
    const promptParts = [
        `Write a short, professional LinkedIn reply to ${targetName}.`,
        "Keep it natural, concise, and directly relevant to the latest message.",
    ];

    if (conversationContext) {
        promptParts.push(`Latest thread context:\n${conversationContext}`);
    }

    return promptParts.join("\n\n");
}

async function fetchReplyFromApi(message, attempt) {
    let lastError = null;
    const requestStartedAt = Date.now();

    for (const endpoint of CHAT_API_ENDPOINTS) {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), API_TIMEOUT_MS);

        pendingApiRequests += 1;

        try {
            logStage("API", `POST ${endpoint} (attempt ${attempt}/${API_RETRY_LIMIT})`);
            const response = await fetch(endpoint, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message }),
                signal: controller.signal,
            });

            const statusInfo = `HTTP ${response.status}`;
            const contentType = response.headers.get("content-type") || "";

            if (!response.ok) {
                throw new Error(statusInfo);
            }

            const responseElapsedMs = Date.now() - requestStartedAt;
            logStage("API", `Response received in ${responseElapsedMs}ms (${statusInfo}).`);

            if (!contentType.includes("application/json")) {
                const rawText = await response.text();
                logStage("API", `Unexpected content-type: ${contentType}. Body preview: ${rawText.slice(0, 120)}`);
                throw new Error("Non-JSON response from API");
            }

            const payload = await response.json();
            const parseElapsedMs = Date.now() - requestStartedAt;
            logStage("API", `JSON parsed in ${parseElapsedMs}ms.`);
            const replyText = cleanText(payload?.reply);

            if (!replyText) {
                logStage("API", `Empty reply field from API (attempt ${attempt}).`);
                throw new Error("Empty reply field");
            }

            return replyText;
        } catch (error) {
            lastError = error;
            const elapsedMs = Date.now() - requestStartedAt;
            if (error?.name === "AbortError" || String(error?.message || "").includes("aborted")) {
                logStage("API", `Request aborted after ${elapsedMs}ms.`);
            } else {
                logStage("API", `Request failed after ${elapsedMs}ms (${error?.message || error}).`);
            }
        } finally {
            clearTimeout(timeoutId);
            pendingApiRequests = Math.max(0, pendingApiRequests - 1);
        }
    }

    throw lastError || new Error("Reply API request failed");
}

function sendDynamicReply(targetName, callback) {
    const prompt = buildReplyPrompt(targetName);
    logStage("API", `Generating reply for ${targetName}`);

    (async () => {
        let replyText = "";

        for (let attempt = 1; attempt <= API_RETRY_LIMIT; attempt += 1) {
            try {
                await humanPause(HUMAN_REPLY_DELAY_MS);
                replyText = await fetchReplyFromApi(prompt, attempt);
                break;
            } catch (error) {
                if (attempt >= API_RETRY_LIMIT) {
                    logStage("API", `Reply generation failed for ${targetName}: ${error?.message || error}`);
                    if (callback) callback(false);
                    return;
                }

                const backoff = API_RETRY_BASE_DELAY_MS * attempt + randomBetween(200, 600);
                logStage("API", `Retrying in ${backoff}ms...`);
                await delay(backoff);
            }
        }

        if (!replyText) {
            logStage("API", `No reply text available for ${targetName}.`);
            if (callback) callback(false);
            return;
        }

        logStage("API", `Reply generated for ${targetName}`);
        sendAutoReply(replyText, targetName, callback);
    })();
}

function composerHasReply(inputBox, replyText) {
    const composerText = cleanText(inputBox?.innerText || inputBox?.textContent);
    return composerText.includes(cleanText(replyText));
}

async function focusComposer(inputBox) {
    if (!inputBox) return false;

    inputBox.click();
    inputBox.focus();
    await delay(COMPOSER_FOCUS_DELAY_MS);

    return document.activeElement === inputBox || inputBox.contains(document.activeElement);
}

async function tryPasteText(normalizedReply) {
    if (!normalizedReply) return false;

    try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
            await navigator.clipboard.writeText(normalizedReply);
        }
    } catch {
        return false;
    }

    try {
        if (typeof document.execCommand === "function") {
            return document.execCommand("paste");
        }
    } catch {
        return false;
    }

    return false;
}

async function populateComposer(inputBox, replyText) {
    const normalizedReply = cleanText(replyText);

    if (!inputBox || !normalizedReply) return false;

    await focusComposer(inputBox);

    try {
        if (typeof document.execCommand === "function") {
            document.execCommand("selectAll", false, null);
            document.execCommand("delete", false, null);
            document.execCommand("insertText", false, normalizedReply);
        }
    } catch {
        // Fallback below.
    }

    if (!composerHasReply(inputBox, normalizedReply)) {
        await focusComposer(inputBox);
        const pasted = await tryPasteText(normalizedReply);

        if (pasted) {
            inputBox.dispatchEvent(new Event("input", { bubbles: true }));
        }
    }

    if (!composerHasReply(inputBox, normalizedReply)) {
        await focusComposer(inputBox);
        inputBox.innerHTML = "";
        inputBox.dispatchEvent(new Event("input", { bubbles: true }));

        for (const char of normalizedReply) {
            inputBox.innerHTML += char === "\n" ? "<br>" : escapeHtml(char);
            const inputEvent = typeof InputEvent === "function"
                ? new InputEvent("input", { bubbles: true, composed: true, inputType: "insertText", data: char })
                : new Event("input", { bubbles: true });
            inputBox.dispatchEvent(inputEvent);
            await delay(randomBetween(...HUMAN_TYPING_DELAY_MS));
        }
    }

    const inputEvent = typeof InputEvent === "function"
        ? new InputEvent("input", { bubbles: true, composed: true, inputType: "insertText", data: normalizedReply })
        : new Event("input", { bubbles: true });
    inputBox.dispatchEvent(inputEvent);
    inputBox.dispatchEvent(new Event("change", { bubbles: true }));

    return composerHasReply(inputBox, normalizedReply);
}

function waitForComposerToClear(replyText, timeout, callback) {
    const startTime = Date.now();
    const normalizedReply = cleanText(replyText);

    function check() {
        const inputBox = document.querySelector(COMPOSER_SELECTOR);
        const composerText = cleanText(inputBox?.innerText || inputBox?.textContent);

        if (!inputBox || !composerText.includes(normalizedReply)) {
            callback(true);
        } else if (Date.now() - startTime < timeout) {
            setTimeout(check, 250);
        } else {
            callback(false);
        }
    }

    check();
}

// === AUTO-REPLY LOGIC ===
function sendAutoReply(replyText, targetName, callback) {
    const normalizedReply = cleanText(replyText);

    async function composeAndSend(attempt) {
        const ready = await new Promise((resolve) => {
            waitForComposerReady(5000, resolve);
        });

        if (!ready) {
            logStage("COMPOSE", "Composer not ready; skipping this attempt.");
            if (callback) callback(false);
            return;
        }

        const inputBox = document.querySelector(COMPOSER_SELECTOR);

        if (!inputBox) {
            logStage("COMPOSE", "Input box not found.");
            if (callback) callback(false);
            return;
        }

        const composed = await populateComposer(inputBox, normalizedReply);

        if (!composed) {
            if (attempt < COMPOSER_RETRY_LIMIT) {
                logStage("COMPOSE", `Composer did not retain reply text; retrying ${attempt + 1}/${COMPOSER_RETRY_LIMIT}`);
                reopenConversation(targetName, (reopened) => {
                    if (!reopened) {
                        logStage("COMPOSE", `Unable to reopen thread for ${targetName}.`);
                        if (callback) callback(false);
                        return;
                    }

                    setTimeout(() => composeAndSend(attempt + 1), 500);
                });
                return;
            }

            logStage("COMPOSE", "Failed to populate the LinkedIn editor.");
            if (callback) callback(false);
            return;
        }

        logStage("COMPOSE", `Reply text inserted for ${normalizedReply.slice(0, 40)}${normalizedReply.length > 40 ? "..." : ""}`);

        waitForSendButton(5000, (sendBtn) => {
            if (!sendBtn) {
                logStage("SEND", "Send button never became enabled.");
                if (callback) callback(false);
                return;
            }

            (async () => {
                await humanPause(HUMAN_SEND_DELAY_MS);
                sendBtn.click();
                logStage("SEND", "Clicked send button.");

                waitForComposerToClear(normalizedReply, SEND_CONFIRMATION_TIMEOUT_MS, (sent) => {
                    if (sent) {
                        logStage("SEND", "Composer cleared after send.");
                        if (callback) setTimeout(() => callback(true), 750);
                    } else {
                        logStage("SEND", "No confirmation after click; treating as failed send.");
                        if (callback) callback(false);
                    }
                });
            })();
        });
    }

    composeAndSend(0);
}

// === HELPER: Wait for send button to become enabled ===
function waitForSendButton(timeout, callback) {
    const startTime = Date.now();

    function check() {
        const buttons = Array.from(document.querySelectorAll(SEND_BUTTON_SELECTOR));
        const btn = buttons.find((button) => button && !button.disabled && button.offsetParent !== null);

        if (btn) {
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