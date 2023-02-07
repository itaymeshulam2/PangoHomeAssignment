from fastapi import APIRouter
from app.resources import cars_controller

api_router = APIRouter()
api_router.include_router(cars_controller.router)
