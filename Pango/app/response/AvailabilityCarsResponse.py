from pydantic import BaseModel
from app.model.Car import Car


class AvailabilityCarsResponse(BaseModel):
    details: list[Car] = []
