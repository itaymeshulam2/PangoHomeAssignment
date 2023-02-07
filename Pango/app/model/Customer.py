from pydantic import BaseModel


class Customer(BaseModel):
    id: int = None
    car_id: int = None