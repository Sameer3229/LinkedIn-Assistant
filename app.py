import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_fireworks import ChatFireworks
from dotenv import load_dotenv

# Environment variables load karein
load_dotenv()
api_key = os.getenv("FIREWORKS_API_KEY")

if not api_key:
    raise ValueError("FIREWORKS_API_KEY not found in .env file")

app = FastAPI()

# --- Middleware Setup ---
# Isse browser requests (CORS) allow hongi
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Security ke liye production mein specify karein (e.g. ["https://www.linkedin.com"])
    allow_credentials=True,
    allow_methods=["*"],  # Sabhi methods (GET, POST, etc.) allow karein
    allow_headers=["*"],  # Sabhi headers allow karein
)

# LLM Initialize karein
llm = ChatFireworks(
    api_key=api_key, 
    model="accounts/fireworks/models/kimi-k2p6"
)

class ChatRequest(BaseModel):
    message: str
    system_prompt: str = ""


def extract_section(message_text: str, section_name: str) -> str:
    marker = f"{section_name}:"
    if marker not in message_text:
        return ""

    tail = message_text.split(marker, 1)[-1]
    for next_header in ["Latest thread context:", "Rules:", "Never use placeholders"]:
        if next_header in tail:
            tail = tail.split(next_header, 1)[0]
            break

    return tail.strip()

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    message_text = (request.message or "").strip()

    if not message_text:
        return {
            "reply": "Could you share the latest message text from the thread so I can respond accurately?"
        }

    latest_inbound = extract_section(message_text, "Latest inbound message")
    if len(latest_inbound) < 2:
        return {
            "reply": "Could you share the latest inbound message from the thread so I can reply accurately?"
        }

    DEFAULT_SYSTEM = (
        "You write LinkedIn direct-message replies on behalf of the account owner. "
        "Output exactly one short reply in plain text (1-2 sentences, max 320 characters). "
        "Use the recipient first name naturally. "
        "NEVER invent, assume, or mention any identity details about the sender - "
        "no profession, no industry, no skills, no role, no company - "
        "unless that information is explicitly given in this system prompt. "
        "If no identity context is given, keep the reply neutral and conversational. "
        "Do not use placeholders or bracket variables. "
        "Do not produce templates, lists, headings, or generic introductions. "
        "If the inbound message is unclear, ask one short clarifying question."
    )

    active_system = request.system_prompt.strip() if request.system_prompt.strip() else DEFAULT_SYSTEM

    system_message = (
        "system",
        active_system
    )

    human_message = ("human", request.message)
    
    response = llm.invoke([system_message, human_message])
    reply_text = (response.content or "").strip()

    if not reply_text:
        return {
            "reply": "Thanks for your message. Could you share a little more context so I can respond clearly?"
        }

    if "[" in reply_text and "]" in reply_text:
        return {
            "reply": "Thanks for your message, and great to connect. Could you share a bit more detail on what you have in mind?"
        }

    return {"reply": reply_text}

if __name__ == "__main__":
    # Note: File ka naam agar main.py hai to yahan "main:app" hona chahiye
    uvicorn.run("app:app", host="0.0.0.0", port=9011, reload=True)