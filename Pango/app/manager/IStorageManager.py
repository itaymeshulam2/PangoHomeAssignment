from datetime import date

from app.model.Car import Car
from app.model.enum.CarType import CarType


class IStorageManager:

    def add_car(self, car: Car):
        pass

    def get_car_by_type(self, car_type: CarType):
        pass

    def get_cars_by_dealership(self, dealership_id: int, start_date: date, end_date: date) -> list[Car]:
        pass

    def get_cars_by_type(self, car_type: CarType, start_date: date, end_date: date) -> list[Car]:
        pass

    def get_cars_by_date(self, start_date: date, end_date: date) -> list[Car]:
        pass