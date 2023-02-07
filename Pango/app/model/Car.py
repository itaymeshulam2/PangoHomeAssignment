from datetime import datetime, date
from pydantic import BaseModel
from app.model.enum.CarType import CarType


class Car(BaseModel):
    car_id: int = None
    dealership_id: int = None
    car_type: CarType = CarType.none
    cost: int = None
    maintenance: bool = False
    start_date: date = None
    end_date: date = None
