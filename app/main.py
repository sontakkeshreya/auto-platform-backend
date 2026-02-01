from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Welcome to Auto Platform Backend!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
