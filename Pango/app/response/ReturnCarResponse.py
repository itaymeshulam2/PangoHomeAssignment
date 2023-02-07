from pydantic import BaseModel


class ReturnCarResponse(BaseModel):
    total_price: float = None
