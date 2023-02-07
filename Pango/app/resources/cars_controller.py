from asyncio import sleep
from datetime import datetime, date

from fastapi import APIRouter, HTTPException

from app.model.enum.CarType import CarType
from app.request.ReturnCarRequest import ReturnCarRequest
from app.response.AvailabilityCarsResponse import AvailabilityCarsResponse
from app.manager.CarsManager import CarsManager
from app.response.ReturnCarResponse import ReturnCarResponse

router = APIRouter(tags=["car_controller"])

@router.get(
    "/availability/cars/type/{car_type}/",
    response_model=AvailabilityCarsResponse,
    status_code=200,
)
async def get_availability_cars_by_type(car_type: CarType, start_date: str, end_date: str):
    await sleep(0.01)
    start_date: date = datetime.strptime(start_date, '%m-%d-%Y').date()
    end_date: date = datetime.strptime(end_date, '%m-%d-%Y').date()
    if start_date >= end_date or start_date <= datetime.today().date():
        raise HTTPException(400, detail='Incorrect date')
    res: AvailabilityCarsResponse = CarsManager().get_availability_cars_by_type(car_type, start_date, end_date)
    if len(res.details) == 0:
        raise HTTPException(404, detail='car type not found')
    return res

@router.get(
    "/availability/cars/dealership/{dealership}/",
    response_model=AvailabilityCarsResponse,
    status_code=200,
)
async def get_availability_cars_by_dealership(dealership: int, start_date: str, end_date: str):
    await sleep(0.01)
    start_date: datetime = datetime.strptime(start_date, '%m-%d-%Y').date()
    end_date: datetime = datetime.strptime(end_date, '%m-%d-%Y').date()
    if start_date >= end_date or start_date <= datetime.today().date():
        raise HTTPException(400, detail='Incorrect date')
    res: AvailabilityCarsResponse = CarsManager().get_availability_cars_by_dealership(dealership, start_date, end_date)
    if len(res.details) == 0:
        raise HTTPException(404, detail='dealership not found')
    return res

@router.get(
    "/availability/cars/",
    response_model=AvailabilityCarsResponse,
    status_code=200,
)
async def get_availability_cars_by_date(start_date: str, end_date: str):
    await sleep(0.01)
    if start_date > end_date or start_date < datetime.today():
        raise HTTPException(400, detail='Incorrect date')
    start_date: datetime = datetime.strptime(start_date, '%m-%d-%Y').date()
    end_date: datetime = datetime.strptime(end_date, '%m-%d-%Y').date()
    if start_date >= end_date or start_date <= datetime.today().date():
        raise HTTPException(400, detail='Incorrect date')
    res: AvailabilityCarsResponse = CarsManager().get_availability_cars_by_date(start_date, end_date)
    if len(res.details) == 0:
        raise HTTPException(404, detail='car not found')
    return res

@router.post(
    "/return/car",
    response_model=ReturnCarResponse,
    status_code=200,
)
async def return_car(return_car: ReturnCarRequest):
    await sleep(0.01)
    res: ReturnCarResponse = CarsManager().return_car(return_car)
    return res
