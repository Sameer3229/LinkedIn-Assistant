console.log("LinkedIn Tracker: Global Monitoring Active...");

// 1. Error Filter
console.error = (function (_error) {
    return function (message) {
        if (typeof message === "string" && (message.includes("chrome-extension") || message.includes("invalid"))) return;
        _error.apply(console, arguments);
    };
})(console.error);

// Track the last inbound signature per conversation so only genuinely new inbound messages are answered.
const conversationState = new Map();
let isProcessing = false;
let pendingApiRequests = 0;
let messagingObserver = null;
let scanDebounceTimer = null;
const CHAT_API_ENDPOINTS = [
    "https://linkedinassitantapi.hnhsofttechsolutions.com/chat",
    // "http://localhost:9011/chat",
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
const COMPOSER_CHUNK_DELAY_MS = [200, 300];
const MAX_REPLY_LENGTH = 800;
const SHORT_REPLY_THRESHOLD = 200;
const COMPOSER_VERIFY_DELAY_MS = [300, 500];
const HEARTBEAT_INTERVAL_MS = 60000;
const SCAN_DEBOUNCE_MS = 700;
const RESCAN_SAME_BADGE_AFTER_MS = 8000;
let lastHeartbeatAt = 0;
let lastScanAt = 0;
const REFRESH_IDLE_POLL_MS = 1500;
const THREAD_READY_TIMEOUT_MS = 6000;
const THREAD_READY_POLL_MS = 300;
let activeSystemPrompt = "";
let activeSystemPromptVersion = "";
let promptContextLoaded = false;

function logStage(stage, message) {
    console.log(`%c[${stage}] ${message}`, "background:#334155;color:white;padding:2px 6px;font-weight:bold;");
}

function randomBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function delay(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

async function safeStorageGet(keys, fallback = {}) {
    try {
        return await chrome.storage.local.get(keys);
    } catch (error) {
        logStage("STORAGE", `Storage read failed: ${error?.message || error}`);
        return fallback;
    }
}

async function refreshSystemPromptContext() {
    const result = await safeStorageGet(["systemPrompt", "systemPromptVersion"], {
        systemPrompt: "",
        systemPromptVersion: "",
    });

    const nextPrompt = cleanText(result.systemPrompt || "");
    const nextVersion = cleanText(result.systemPromptVersion || "");

    if (promptContextLoaded && nextVersion && nextVersion !== activeSystemPromptVersion) {
        // Only reset inbound signatures so conversations are re-evaluated
        // while preserving lastSentText for the self-reply guard.
        for (const [key, state] of conversationState.entries()) {
            conversationState.set(key, {
                ...state,
                lastInboundSignature: "",
            });
        }
        logStage("PROMPT", "System prompt changed; reset inbound signatures (lastSentText preserved).");
    }

    activeSystemPrompt = nextPrompt;
    activeSystemPromptVersion = nextVersion;
    promptContextLoaded = true;

    return {
        systemPrompt: activeSystemPrompt,
        systemPromptVersion: activeSystemPromptVersion,
    };
}

chrome.storage.onChanged.addListener((changes, areaName) => {
    if (areaName !== "local") return;

    if (changes.systemPrompt || changes.systemPromptVersion) {
        refreshSystemPromptContext().catch((error) => {
            logStage("STORAGE", `Prompt refresh failed: ${error?.message || error}`);
        });
    }
});

function queueScan(triggerSource, delayMs = SCAN_DEBOUNCE_MS) {
    if (scanDebounceTimer) {
        clearTimeout(scanDebounceTimer);
    }

    scanDebounceTimer = setTimeout(() => {
        scanDebounceTimer = null;
        finalScraper(triggerSource);
    }, delayMs);
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

function getCardName(card) {
    return cleanText(card?.querySelector('h3.msg-conversation-card__participant-names')?.innerText || "");
}

function getConversationKeyFromCard(card, fallbackName = "") {
    const link =
        card?.closest?.('a[href*="/messaging/thread/"]') ||
        card?.querySelector?.('a[href*="/messaging/thread/"]') ||
        null;
    const href = link?.getAttribute?.('href') || "";
    const match = href.match(/thread\/([^/?#]+)/i);

    if (match?.[1]) {
        return match[1];
    }

    return cleanText(fallbackName).toLowerCase();
}

function getActiveConversationKey(targetName = "") {
    const activeSelectors = [
        '.msg-conversation-card--active',
        '[aria-current="true"]',
        '.msg-conversation-listitem__link.active',
    ];

    for (const selector of activeSelectors) {
        const node = document.querySelector(selector);
        const key = getConversationKeyFromCard(node, getCardName(node));
        if (key) return key;
    }

    const pathMatch = window.location.pathname.match(/\/messaging\/thread\/([^/]+)/i);
    if (pathMatch?.[1]) {
        return pathMatch[1];
    }

    return cleanText(targetName).toLowerCase();
}

function hasUnreadConversationMarkers() {
    return Boolean(
        document.querySelector('.msg-conversation-card__message-snippet--unread') ||
        document.querySelector('.msg-conversation-card__unread-count') ||
        document.querySelector('h3.msg-conversation-card__participant-names.t-bold')
    );
}

function looksLikeMessagingMutation(mutation) {
    const target = mutation.target;
    if (!(target instanceof Element)) return false;

    const relevantSelectors = [
        '.msg-conversation-card__message-snippet--unread',
        '.msg-conversation-card__unread-count',
        '.msg-s-event-listitem',
        '.msg-s-message-group',
        '.notification-badge--show',
        '.msg-conversation-card__content--selectable',
    ];

    if (relevantSelectors.some((selector) => target.matches?.(selector) || target.closest?.(selector))) {
        return true;
    }

    for (const node of mutation.addedNodes || []) {
        if (!(node instanceof Element)) continue;
        if (relevantSelectors.some((selector) => node.matches?.(selector) || node.querySelector?.(selector))) {
            return true;
        }
    }

    return false;
}

function ensureMessagingObserver() {
    if (messagingObserver) return;

    const root = document.body;
    if (!root) return;

    messagingObserver = new MutationObserver((mutations) => {
        if (isProcessing) return;

        for (const mutation of mutations) {
            if (looksLikeMessagingMutation(mutation)) {
                queueScan("mutation", 500);
                break;
            }
        }
    });

    messagingObserver.observe(root, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ["class", "aria-label"],
    });

    logStage("OBSERVE", "Messaging mutation observer enabled.");
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

function finalScraper(triggerSource = "poll") {
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
    const onMessagingPage = window.location.pathname.includes("/messaging");
    const badgeSignature = `${badgeCount || "?"}:${hasAriaNotification ? "aria" : "dom"}`;
    const shouldRescanSameBadge = now - lastScanAt > RESCAN_SAME_BADGE_AFTER_MS;

    if (onMessagingPage && hasUnreadConversationMarkers()) {
        lastScanAt = now;
        logStage("SCAN", `Unread marker trigger (${triggerSource}).`);
        collectAndProcess(0, `inbox:${triggerSource}`);
        return;
    }

    if (hasNotification) {
        const count = badgeCount || ariaLabel.match(/(\d+)\s*new/)?.[1] || "?";
        if (window.lastCount !== badgeSignature || shouldRescanSameBadge) {
            window.lastCount = badgeSignature;
            lastScanAt = now;
            logStage("SCAN", `Notification detected: ${count} (${triggerSource})`);
            msgLink.click();
            waitForInboxReady(10000, (ready) => {
                if (!ready) {
                    logStage("WAIT", "Messaging inbox did not become ready in time; will retry on the next scan.");
                    window.lastCount = null;
                    return;
                }

                logStage("SCAN", "Messaging inbox is ready; collecting unread chats.");
                collectAndProcess(0, `badge:${triggerSource}`);
            });
        }
    }
}

function scheduleRefreshAfterIdle() {
    const startTime = Date.now();

    function check() {
        if (pendingApiRequests === 0) {
            logStage("REFRESH", "Idle state reached; scheduling next scan.");
            isProcessing = false;
            window.lastCount = null;
            queueScan("idle", 1500);
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
function collectAndProcess(retryCount = 0, triggerSource = "direct") {
    if (isProcessing && retryCount === 0) return;
    if (!isProcessing) isProcessing = true;

    const allCards = document.querySelectorAll(MESSAGE_CARD_SELECTOR);
    const unreadConversations = [];

    allCards.forEach(card => {
        const hasUnreadSnippet = card.querySelector('.msg-conversation-card__message-snippet--unread') !== null;
        const hasUnreadBadge = card.querySelector('.msg-conversation-card__unread-count') !== null;
        const nameEl = card.querySelector('h3.msg-conversation-card__participant-names');
        const isBoldName = nameEl?.classList?.contains('t-bold');

        if (hasUnreadSnippet || hasUnreadBadge || isBoldName) {
            const name = nameEl?.innerText?.trim() || "";
            const key = getConversationKeyFromCard(card, name);
            const exists = unreadConversations.some((conversation) => conversation.key === key);

            if (name && key && !exists) {
                unreadConversations.push({ key, name });
                console.log(`%c[FOUND] Unread: ${name} (${key})`, "background:#f59e0b;color:black;padding:2px 6px;");
            }
        }
    });

    if (allCards.length === 0 && retryCount < INBOX_READY_RETRY_LIMIT) {
        logStage("WAIT", `Conversation list not ready yet; retrying scan ${retryCount + 1}/${INBOX_READY_RETRY_LIMIT}`);
        setTimeout(() => collectAndProcess(retryCount + 1, triggerSource), INBOX_READY_RETRY_DELAY_MS);
        return;
    }

    if (unreadConversations.length === 0) {
        if (retryCount < INBOX_READY_RETRY_LIMIT) {
            logStage("WAIT", `Unread markers not visible yet; rescanning ${retryCount + 1}/${INBOX_READY_RETRY_LIMIT}`);
            setTimeout(() => collectAndProcess(retryCount + 1, triggerSource), INBOX_READY_RETRY_DELAY_MS);
            return;
        }

        logStage("INFO", `No unread chats to reply (trigger: ${triggerSource}).`);
        window.lastCount = null;
        isProcessing = false;
        return;
    }

    logStage("QUEUE", `${unreadConversations.length} unread chat(s) to process: ${unreadConversations.map((c) => c.name).join(', ')}`);

    // Start processing by name, one by one
    processByName(unreadConversations, 0);
}

// === STEP 2: Find card by NAME (fresh DOM lookup each time), click it, reply ===
function processByName(conversations, index) {
    if (index >= conversations.length) {
        logStage("DONE", `All ${conversations.length} unread chats processed.`);
        isProcessing = false;
        window.lastCount = null;
        // Wait full HUMAN_REFRESH_DELAY_MS before next scan to give LinkedIn time to clear unread markers
        const fullDelay = randomBetween(...HUMAN_REFRESH_DELAY_MS);
        logStage("REFRESH", `Waiting ${fullDelay}ms before next scan to let LinkedIn clear unread markers.`);
        setTimeout(() => {
            queueScan("queue-complete");
        }, fullDelay);
        return;
    }

    const target = conversations[index];
    const targetName = target.name;
    const targetKey = target.key;
    logStage("PROCESS", `${index + 1}/${conversations.length} ${targetName} (${targetKey})`);

    // Fresh DOM search: find the conversation card by matching the name text
    const card = findCardByName(targetName, targetKey);

    if (!card) {
        logStage("WARN", `Card not found for "${targetName}". Continuing queue without marking replied.`);
        setTimeout(() => processByName(conversations, index + 1), 1000);
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
                    setTimeout(() => processByName(conversations, index + 1), 2000);
                    return;
                }

                waitForElement(COMPOSER_SELECTOR, 8000, (inputBox) => {
                    if (!inputBox) {
                        logStage("WARN", `Input box not found after reopen for ${targetName}.`);
                        setTimeout(() => processByName(conversations, index + 1), 2000);
                        return;
                    }

                    setTimeout(() => {
                        sendDynamicReply(targetName, targetKey, (result) => {
                            if (result?.success && result?.skipped) {
                                logStage("SKIP", `${index + 1}/${conversations.length} ${targetName} (same inbound signature)`);
                            } else if (result?.success) {
                                logStage("SENT", `${index + 1}/${conversations.length} ${targetName}`);
                            } else {
                                logStage("FAILED", `${index + 1}/${conversations.length} ${targetName}`);
                            }

                            setTimeout(() => processByName(conversations, index + 1), 3000);
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
            setTimeout(() => processByName(conversations, index + 1), 2000);
            return;
        }

        // Let LinkedIn fully settle
        setTimeout(() => {
            sendDynamicReply(targetName, targetKey, (result) => {
                if (result?.success && result?.skipped) {
                    logStage("SKIP", `${index + 1}/${conversations.length} ${targetName} (same inbound signature)`);
                } else if (result?.success) {
                    logStage("SENT", `${index + 1}/${conversations.length} ${targetName}`);
                } else {
                    logStage("FAILED", `${index + 1}/${conversations.length} ${targetName}`);
                }

                // Wait for LinkedIn to update, then process next name
                setTimeout(() => processByName(conversations, index + 1), 3000);
            });
        }, 1500);
    });
    });
}

// === HELPER: Find conversation card by matching name text ===
function findCardByName(targetName, targetKey = "") {
    const allCards = document.querySelectorAll('.msg-conversation-card__content--selectable');

    if (targetKey) {
        for (let i = 0; i < allCards.length; i++) {
            const key = getConversationKeyFromCard(allCards[i], getCardName(allCards[i]));
            if (key === targetKey) {
                return allCards[i];
            }
        }
    }
    
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

function getMessageListRoot() {
    return (
        document.querySelector('.msg-s-message-list') ||
        document.querySelector('.msg-s-message-list-content') ||
        document.querySelector('[data-test-id="message-list"]') ||
        document.querySelector('[class*="msg-s-message-list"]') ||
        document.querySelector('.msg-thread') ||
        null
    );
}

function waitForThreadContentReady(timeout, callback) {
    const startTime = Date.now();

    function check() {
        const root = getMessageListRoot();
        const rootText = cleanText(root?.innerText || root?.textContent);

        if (root && rootText.length > 0) {
            callback(true);
        } else if (Date.now() - startTime < timeout) {
            setTimeout(check, THREAD_READY_POLL_MS);
        } else {
            callback(false);
        }
    }

    check();
}

function extractConversationData() {
    const root = getMessageListRoot();
    if (!root) return { messages: [], latestInbound: "", debugStats: {} };

    const messages = [];
    const inboundMessages = [];
    const debugStats = {};
    const messageSelectors = [
        '.msg-s-event-listitem__body',
        '.msg-s-message-group__message-text',
        '[data-test-id="message-content"]',
        '[data-test-id="message-bubble"]',
        '.msg-s-event-listitem__message-bubble',
        '.msg-s-message-group__message-text span',
    ];

    const timestampPatterns = [
        /\b\d{1,2}:\d{2}\b/i,
        /\b(today|yesterday)\b/i,
        /\b(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)\b/i,
    ];

    function isTimestampText(text) {
        return timestampPatterns.some((pattern) => pattern.test(text));
    }

    function isInboundNode(node) {
        const wrapper = node?.closest?.('.msg-s-message-group, .msg-s-event-listitem, .msg-s-message-list__event');
        if (!wrapper) return false;

        const eventContainer = node?.closest?.('.msg-s-event-with-indicator')
            || wrapper?.closest?.('.msg-s-event-with-indicator');
        if (eventContainer) {
            const sendingIndicator = eventContainer.querySelector('[class*="sending-indicator"]');
            if (sendingIndicator) {
                return false;
            }
        }

        const outboundMarkers = [
            'msg-s-message-group--me',
            'msg-s-message-group--self',
            'msg-s-event-listitem--self',
            'msg-s-event-listitem--me',
            'msg-s-message-group--outgoing',
            'msg-s-event-listitem--outgoing',
        ];

        const inboundMarkers = [
            'msg-s-event-listitem--other',
            'msg-s-message-group--other',
        ];

        let current = wrapper;
        while (current && current instanceof Element) {
            const classList = current.classList || [];

            if (outboundMarkers.some((marker) => classList.contains(marker))) {
                return false;
            }

            if (inboundMarkers.some((marker) => classList.contains(marker))) {
                return true;
            }

            if (current.querySelector?.('a.msg-s-event-listitem__link')) {
                return true;
            }

            current = current.parentElement;
        }

        return false;
    }

    function pushMessage(node) {
        if (node?.getAttribute?.("aria-hidden") === "true") return;

        const trimmed = cleanText(node.innerText || node.textContent);
        if (!trimmed || trimmed.length < 2) return;
        if (isTimestampText(trimmed)) return;

        if (!messages.includes(trimmed)) messages.push(trimmed);
        if (isInboundNode(node) && !inboundMessages.includes(trimmed)) inboundMessages.push(trimmed);
    }

    for (const selector of messageSelectors) {
        const messageNodes = root.querySelectorAll(selector);
        debugStats[selector] = messageNodes.length;
        messageNodes.forEach((node) => pushMessage(node));
    }

    if (messages.length === 0) {
        const globalNodes = document.querySelectorAll('.msg-s-event-listitem__body, .msg-s-message-group__message-text');
        debugStats["__global__"] = globalNodes.length;
        globalNodes.forEach((node) => pushMessage(node));
    }

    const latestInbound = inboundMessages.length > 0 ? inboundMessages[inboundMessages.length - 1] : "";
    return { messages, latestInbound, debugStats };
}

function getFirstName(name) {
    const cleaned = cleanText(name);
    if (!cleaned) return "there";
    return cleaned.split(/\s+/)[0];
}

function buildInboundSignature(latestInbound, messages) {
    const normalizedInbound = cleanText(latestInbound).toLowerCase();
    return normalizedInbound;
}

function buildReplyPrompt(targetName) {
    const { messages, latestInbound } = extractConversationData();
    const firstName = getFirstName(targetName);
    const promptParts = [
        "Write a short, professional LinkedIn DM reply.",
        `Recipient name: ${targetName}`,
        `Recipient first name: ${firstName}`,
        "Rules: 1-2 short sentences, natural tone, directly answer the latest inbound message, no bullet points, no templates.",
        "Never use placeholders like [Name], [Company], [your role], [industry], or bracket variables.",
    ];

    if (latestInbound) {
        promptParts.push(`Latest inbound message:\n${latestInbound}`);
    }

    if (messages.length > 0) {
        promptParts.push(`Latest thread context:\n${messages.slice(-3).join("\n\n")}`);
    } else {
        promptParts.push("If no context is available, respond with a brief request for clarification.");
    }

    return promptParts.join("\n\n");
}

async function fetchReplyFromApi(message, attempt, customSystemPrompt) {
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
                body: JSON.stringify({ message, system_prompt: customSystemPrompt || "" }),
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

function sendDynamicReply(targetName, conversationKey, callback) {
    const prompt = buildReplyPrompt(targetName);
    logStage("API", `Generating reply for ${targetName}`);

    (async () => {
        const ready = await new Promise((resolve) => {
            waitForThreadContentReady(THREAD_READY_TIMEOUT_MS, resolve);
        });

        if (!ready) {
            logStage("CONTEXT", `Thread content not ready for ${targetName}; skipping API call.`);
            if (callback) callback(false);
            return;
        }

        const { messages, latestInbound, debugStats } = extractConversationData();
        if (messages.length === 0) {
            logStage("CONTEXT", `No message nodes found for ${targetName}. Selector counts: ${JSON.stringify(debugStats)}`);
            if (callback) callback(false);
            return;
        }

        if (!latestInbound) {
            logStage("CONTEXT", `No inbound message detected for ${targetName}; skipping API call.`);
            if (callback) callback({ success: false, reason: "missing-inbound" });
            return;
        }

        const existingStateEarly = conversationState.get(
            cleanText(conversationKey || getActiveConversationKey(targetName)).toLowerCase()
        ) || {};
        if (
            existingStateEarly.lastSentText &&
            cleanText(latestInbound).toLowerCase().includes(
                cleanText(existingStateEarly.lastSentText).toLowerCase().slice(0, 60)
            )
        ) {
            logStage("DEDUPE", `Latest inbound matches our own last sent reply for ${targetName}; skipping.`);
            if (callback) callback({ success: true, skipped: true, reason: "self-reply-guard" });
            return;
        }

        const effectiveConversationKey = cleanText(conversationKey || getActiveConversationKey(targetName));
        const stateKey = cleanText(effectiveConversationKey || targetName).toLowerCase();
        const existingState = conversationState.get(stateKey) || {};

        const inboundSignature = buildInboundSignature(latestInbound, messages);
        const previousSignature = existingState.lastInboundSignature || "";

        if (previousSignature && previousSignature === inboundSignature) {
            logStage("DEDUPE", `Skipping ${targetName}; inbound signature unchanged (${stateKey}).`);
            conversationState.set(stateKey, {
                ...existingState,
                lastInboundSignature: previousSignature,
                lastSentAt: existingState.lastSentAt || Date.now(),
            });
            if (callback) callback({ success: true, skipped: true, reason: "same-inbound" });
            return;
        }

        if (!previousSignature) {
            logStage(
                "DEDUPE",
                `Inbound signature for ${targetName} (${stateKey}): first time, new=${inboundSignature.slice(0, 24)}`
            );
        } else {
            logStage(
                "DEDUPE",
                `Inbound signature changed for ${targetName} (${stateKey}): old=${previousSignature.slice(0, 24)} new=${inboundSignature.slice(0, 24)}`
            );
        }

        const composerReady = await new Promise((resolve) => {
            waitForComposerReady(5000, resolve);
        });

        if (!composerReady) {
            logStage("COMPOSE", `Composer not ready for ${targetName}; skipping API call.`);
            if (callback) callback({ success: false, reason: "composer-not-ready" });
            return;
        }

        const inputBox = document.querySelector(COMPOSER_SELECTOR);
        const focused = await focusComposer(inputBox);
        if (!focused) {
            logStage("COMPOSE", `Composer focus failed for ${targetName}; skipping API call.`);
            if (callback) callback({ success: false, reason: "focus-failed" });
            return;
        }

        let replyText = "";
                const promptContext = await refreshSystemPromptContext();
                const storedPrompt = promptContext.systemPrompt || "";

        for (let attempt = 1; attempt <= API_RETRY_LIMIT; attempt += 1) {
            try {
                await humanPause(HUMAN_REPLY_DELAY_MS);
                replyText = await fetchReplyFromApi(prompt, attempt, storedPrompt);
                break;
            } catch (error) {
                if (attempt >= API_RETRY_LIMIT) {
                    logStage("API", `Reply generation failed for ${targetName}: ${error?.message || error}`);
                    if (callback) callback({ success: false, reason: "api-failed" });
                    return;
                }

                const backoff = API_RETRY_BASE_DELAY_MS * attempt + randomBetween(200, 600);
                logStage("API", `Retrying in ${backoff}ms...`);
                await delay(backoff);
            }
        }

        if (!replyText) {
            logStage("API", `No reply text available for ${targetName}.`);
            if (callback) callback({ success: false, reason: "empty-reply" });
            return;
        }

        const sentReplyText = cleanText(replyText);

        logStage("API", `Reply generated for ${targetName}`);
        sendAutoReply(replyText, targetName, (success) => {
            if (success) {
                conversationState.set(stateKey, {
                    lastInboundSignature: inboundSignature,
                    lastSentAt: Date.now(),
                    lastSentText: sentReplyText,
                    lastProcessedAt: Date.now(),
                    skipCount: 0
                });
            }

            if (callback) {
                callback({
                    success,
                    skipped: false,
                    stateKey,
                });
            }
        });
    })();
}

function composerHasReply(inputBox, replyText) {
    const composerText = cleanText(inputBox?.innerText || inputBox?.textContent);
    return replyMatchesSnippet(composerText, replyText);
}

function getReplySnippets(text) {
    const normalized = cleanText(text);
    if (!normalized) return { head: "", tail: "" };

    const head = normalized.slice(0, 50);
    const tail = normalized.length > 50 ? normalized.slice(-50) : normalized;
    return { head, tail };
}

function replyMatchesSnippet(composerText, replyText) {
    const normalizedComposer = cleanText(composerText);
    const { head, tail } = getReplySnippets(replyText);

    if (!normalizedComposer || !head) return false;

    if (head && tail) {
        return normalizedComposer.includes(head) && normalizedComposer.includes(tail);
    }

    return normalizedComposer.includes(head);
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

function chunkReplyText(text) {
    const normalized = cleanText(text);
    if (!normalized) return [];

    const rawChunks = normalized.split(/\n\n+/).map((chunk) => chunk.trim()).filter(Boolean);
    return rawChunks.length > 0 ? rawChunks : [normalized];
}

function clearComposer(inputBox) {
    if (!inputBox) return;

    // Select all text and delete via keyboard events — React hears this and clears its state
    inputBox.focus();
    document.execCommand("selectAll", false, null);
    document.execCommand("delete", false, null);

    // Fire an input event so React reconciles the empty state
    inputBox.dispatchEvent(new InputEvent("input", { bubbles: true, composed: true }));
}

// Core helper: insert text into a contenteditable in a way React's event system recognises.
// Uses DataTransfer + ClipboardEvent so LinkedIn's ProseMirror/React sees a real paste
// and updates its internal state — which is what enables the Send button.
async function insertTextViaClipboardEvent(inputBox, text) {
    inputBox.focus();

    const dt = new DataTransfer();
    dt.setData("text/plain", text);

    const pasteEvent = new ClipboardEvent("paste", {
        bubbles: true,
        cancelable: true,
        clipboardData: dt,
    });

    inputBox.dispatchEvent(pasteEvent);

    // Wait for React to reconcile
    await delay(80);
    const currentText = cleanText(inputBox.innerText || inputBox.textContent);
    if (currentText.includes(cleanText(text).slice(0, 30))) return true;

    // Fallback: execCommand insertText (still works in Chrome extension content scripts)
    inputBox.focus();
    return document.execCommand("insertText", false, text);
}

async function populateComposer(inputBox, replyText) {
    let normalizedReply = cleanText(replyText);

    if (!inputBox || !normalizedReply) return false;

    if (normalizedReply.length > MAX_REPLY_LENGTH) {
        normalizedReply = `${normalizedReply.slice(0, MAX_REPLY_LENGTH)}...`;
    }

    await focusComposer(inputBox);
    clearComposer(inputBox);
    await delay(150);

    // Strategy 1: ClipboardEvent paste (preferred — React sees it and enables Send button)
    const inserted = await insertTextViaClipboardEvent(inputBox, normalizedReply);

    if (!inserted) {
        // Strategy 2: execCommand character-by-character (last resort)
        await focusComposer(inputBox);
        clearComposer(inputBox);
        await delay(100);

        for (const char of normalizedReply) {
            document.execCommand("insertText", false, char);
            await delay(randomBetween(...HUMAN_TYPING_DELAY_MS));
        }
    }

    await delay(randomBetween(...COMPOSER_VERIFY_DELAY_MS));
    return replyMatchesSnippet(inputBox?.innerText || inputBox?.textContent, normalizedReply);
}

function findLatestOutgoingBubble(replyText) {
    const root = getMessageListRoot();
    if (!root) return null;

    const outgoingSelectors = [
        '.msg-s-message-group--me .msg-s-message-group__message-text',
        '.msg-s-event-listitem--self .msg-s-event-listitem__body',
        '.msg-s-message-group--me [data-test-id="message-content"]',
    ];

    const { head, tail } = getReplySnippets(replyText);

    for (const selector of outgoingSelectors) {
        const nodes = Array.from(root.querySelectorAll(selector));
        for (const node of nodes.reverse()) {
            const text = cleanText(node.innerText || node.textContent);
            if (text && text.includes(head) && text.includes(tail)) {
                return node;
            }
        }
    }

    return null;
}

function waitForSendConfirmation(replyText, timeout, callback) {
    const startTime = Date.now();

    function check() {
        const inputBox = document.querySelector(COMPOSER_SELECTOR);
        const composerText = cleanText(inputBox?.innerText || inputBox?.textContent);
        const bubble = findLatestOutgoingBubble(replyText);

        if (bubble || !composerText) {
            callback(true);
        } else if (Date.now() - startTime < timeout) {
            setTimeout(check, 250);
        } else {
            callback(false);
        }
    }

    check();
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
    let normalizedReply = cleanText(replyText);

    if (normalizedReply.length > MAX_REPLY_LENGTH) {
        normalizedReply = `${normalizedReply.slice(0, MAX_REPLY_LENGTH)}...`;
    }

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
                if (attempt < 2) {
                    setTimeout(() => composeAndSend(attempt + 1), 500);
                    return;
                }

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

                waitForSendConfirmation(normalizedReply, SEND_CONFIRMATION_TIMEOUT_MS, (sent) => {
                    if (sent) {
                        logStage("SEND", "Composer cleared after send.");
                        if (callback) {
                            setTimeout(() => callback(true), 750);
                            // Click card again after 1000ms to trigger LinkedIn read receipt
                            setTimeout(() => {
                                const card = findCardByName(targetName);
                                if (card) {
                                    card.click();
                                    logStage("SEND", "Clicked card to trigger LinkedIn read receipt (first click).");
                                    // Second click after a short dwell to force LinkedIn to register the read state.
                                    setTimeout(() => {
                                        const cardAgain = findCardByName(targetName);
                                        if (cardAgain) {
                                            cardAgain.click();
                                            logStage("SEND", "Clicked card again to confirm read receipt.");
                                        }
                                    }, 1500);
                                }
                            }, 1000);
                        }
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

ensureMessagingObserver();
refreshSystemPromptContext().catch((error) => {
    logStage("STORAGE", `Initial prompt load failed: ${error?.message || error}`);
});
finalScraper("startup");
setInterval(() => {
    ensureMessagingObserver();
    finalScraper("poll");
}, 3000);