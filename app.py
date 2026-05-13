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

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    system_message = (
        "system", 
        "Main ek behtreen HR recruiter hun jo enterprises ko "
        "solutions or strategies provide krta hun hiring related."
    )
    human_message = ("human", request.message)
    
    response = llm.invoke([system_message, human_message])
    return {"reply": response.content}

if __name__ == "__main__":
    # Note: File ka naam agar main.py hai to yahan "main:app" hona chahiye
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)