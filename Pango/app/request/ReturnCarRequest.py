from pydantic import BaseModel


class ReturnCarRequest(BaseModel):
    car_id: int = None
    dealership_id: int = None

