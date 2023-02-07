from datetime import datetime, date

from app.manager.IStorageManager import IStorageManager
from app.manager.storage_managers.DBStorageManager import DBStorageManager
from app.model.Car import Car
from app.model.enum.CarType import CarType
from app.request.ReturnCarRequest import ReturnCarRequest
from app.response.AvailabilityCarsResponse import AvailabilityCarsResponse
from app.response.ReturnCarResponse import ReturnCarResponse


class CarsManager:
    storage_manager: IStorageManager = DBStorageManager()

    def return_car(self, return_car: ReturnCarRequest) -> ReturnCarResponse:
        res: ReturnCarResponse = ReturnCarResponse()
        res.total_price = self.__return_car(return_car)
        return res

    def get_availability_cars_by_type(self, car_type: CarType, start_date: date, end_date: date) -> AvailabilityCarsResponse:
        res: AvailabilityCarsResponse = AvailabilityCarsResponse()
        res.details.extend(self.__get_car_by_type(car_type, start_date, end_date))
        return res

    def get_availability_cars_by_dealership(self, dealership_id: int, start_date: date, end_date: date) -> AvailabilityCarsResponse:
        res: AvailabilityCarsResponse = AvailabilityCarsResponse()
        res.details.extend(self.__get_cars_by_dealership(dealership_id, start_date, end_date))
        return res

    def get_availability_cars_by_date(self, start_date: date, end_date: date) -> AvailabilityCarsResponse:
        res: AvailabilityCarsResponse = AvailabilityCarsResponse()
        res.details.extend(self.__get_cars_by_date(start_date, end_date))
        return res

    def __return_car(self, return_car: ReturnCarRequest) -> float:
        return self.storage_manager.return_car_and_get_total_price(return_car)

    def __get_cars_by_date(self, start_date: date, end_date: date) -> list[Car]:
        res: list[Car] = None
        res = self.storage_manager.get_cars_by_date(start_date, end_date)
        return res

    def __get_cars_by_dealership(self, dealership_id: int, start_date: date, end_date: date) -> list[Car]:
        res: list[Car] = None
        res = self.storage_manager.get_cars_by_dealership(dealership_id, start_date, end_date)
        return res

    def __get_car_by_type(self, car_type: CarType, start_date: date, end_date: date) -> list[Car]:
        res: list[Car] = None
        res = self.storage_manager.get_cars_by_type(car_type, start_date, end_date)
        return res
