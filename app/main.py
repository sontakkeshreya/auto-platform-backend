from fastapi import FastAPI,Depends
from app.api.v1.router import api_router
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    print("✅ Database connected")
    yield
    # Shutdown code (optional)

app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Welcome to Auto Platform Backend!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
