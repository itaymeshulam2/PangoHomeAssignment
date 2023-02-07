import pathlib
from datetime import datetime, date

from app.manager.IStorageManager import IStorageManager
from app.model.Car import Car
from app.model.enum.CarType import CarType
from app.request.ReturnCarRequest import ReturnCarRequest


class DBStorageManager(IStorageManager):
    cars: list[Car] = []

    def __init__(self):
        self.add_car()

    def add_car(self):
        car: Car = Car()
        car.car_id = 1
        car.dealership_id = 1
        car.car_type: CarType = CarType.ford
        car.cost = 20
        car.maintenance = True
        self.cars.append(car)

        car: Car = Car()
        car.car_id = 2
        car.dealership_id = 2
        car.car_type: CarType = CarType.farai
        car.cost = 20
        car.start_date = datetime.strptime('09-19-2022', '%m-%d-%Y').date()
        car.end_date = datetime.strptime('09-25-2022', '%m-%d-%Y').date()
        car.maintenance = False
        self.cars.append(car)

    def get_cars_by_date(self, start_date: date, end_date: date) -> list[Car]:
        res: list[Car] = []
        for car in self.cars:
            if car.maintenance is False:
                if car.start_date is None and car.end_date is None:
                    res.append(car)
                elif car.end_date is not None and car.end_date < start_date:
                    res.append(car)

        return res

    def get_cars_by_dealership(self, dealership_id: int, start_date: date, end_date: date) -> list[Car]:
        res: list[Car] = []
        for car in self.cars:
            if dealership_id == car.dealership_id and car.maintenance is False:
                if car.start_date is None and car.end_date is None:
                    res.append(car)
                elif car.end_date is not None and car.end_date < start_date:
                    res.append(car)

        return res

    def get_cars_by_type(self, car_type: CarType, start_date: date, end_date: date) -> list[Car]:
        res: list[Car] = []
        for car in self.cars:
            if car_type == car.car_type and car.maintenance is False:
                if car.start_date is None and car.end_date is None:
                    res.append(car)
                elif car.end_date is not None and car.end_date < start_date:
                    res.append(car)

        return res

    def return_car_and_get_total_price(self, return_car: ReturnCarRequest) -> float:
        res: float = 0
        for car in self.cars:
            if car.car_id == return_car.car_id:
                res = self.__get_total_price(car)
                car.start_date = None
                car.end_date = None
                car.dealership_id = return_car.dealership_id
                break

        return res

    def __get_total_price(self, car: Car) -> float:
        res: float = 0
        delta: int = (car.end_date - car.start_date).days
        if delta > 5:
            res = car.cost * delta * 0.8
        else:
            res = car.cost * delta
        return res