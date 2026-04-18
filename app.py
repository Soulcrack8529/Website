from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import random

app = FastAPI(title="My Free API", description="Free API on Railway", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "🚀 API is live on Railway!",
        "endpoints": ["/hello/{name}", "/random-number", "/add?a=1&b=2", "/joke", "/health"]
    }

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello {name}! Welcome to Railway API"}

@app.get("/random-number")
def random_number():
    return {"random": random.randint(1, 1000)}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/joke")
def joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the developer go broke? Because he used up all his cache!",
        "What is a programmer's favorite place? The Foo Bar!"
    ]
    return {"joke": random.choice(jokes)}

@app.get("/health")
def health():
    return {"status": "healthy", "uptime": "running smoothly"}
