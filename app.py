from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
import os
import random
from typing import Optional

app = FastAPI(title="My Secure API", description="API with Key Authentication", version="1.0.0")

# CORS allow kar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Key - Railway Variables se lega
VALID_API_KEY = os.environ.get("API_KEY", "default-key-change-me")

# Key verify karne ka function
def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API Key missing! Please provide X-API-Key header")
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key!")
    return True

# Public routes (bina key ke)
@app.get("/")
def home():
    return {
        "message": "🚀 API is live on Railway!",
        "note": "Most endpoints require API key. Add header: X-API-Key: your-key",
        "public_endpoints": ["/", "/health"],
        "protected_endpoints": ["/hello/{name}", "/random-number", "/add", "/joke"]
    }

@app.get("/health")
def health():
    return {"status": "healthy", "uptime": "running smoothly"}

# Protected routes (key chahiye)
@app.get("/hello/{name}")
def hello(name: str, auth: bool = Depends(verify_api_key)):
    return {"message": f"Hello {name}! Welcome to Secure Railway API"}

@app.get("/random-number")
def random_number(auth: bool = Depends(verify_api_key)):
    return {"random": random.randint(1, 1000)}

@app.get("/add")
def add(a: int, b: int, auth: bool = Depends(verify_api_key)):
    return {"result": a + b}

@app.get("/joke")
def joke(auth: bool = Depends(verify_api_key)):
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the developer go broke? Because he used up all his cache!",
        "What is a programmer's favorite place? The Foo Bar!",
        "Why do Java developers wear glasses? Because they can't C#!"
    ]
    return {"joke": random.choice(jokes)}
