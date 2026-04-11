from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import contact, health

app = FastAPI(title="Tyler Du Portfolio API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://whoistylerdu.com",
        "https://www.whoistylerdu.com",
        "http://localhost:5173",
    ],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
    max_age=3600,
)

app.include_router(health.router, prefix="/api")
app.include_router(contact.router, prefix="/api")
