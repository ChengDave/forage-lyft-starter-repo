from car_factory import CarFactory
from datetime import datetime

class Glissade:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.__current_date = datetime.today().date()
        self.__car = CarFactory.create_glissade(self.__current_date, last_service_date, current_mileage, last_service_mileage)

    def needs_service(self):
        return self.__car.needs_service()