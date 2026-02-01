from fastapi import APIRouter
from app.api.v1.endpoints import vehicle

api_router = APIRouter()
api_router.include_router(vehicle.router, prefix="/vehicle", tags=["vehicle"])

@api_router.get("/")
def root():
    return {"message": "v1 api is alive"}
