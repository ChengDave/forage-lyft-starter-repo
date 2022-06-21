from car_factory import CarFactory
from datetime import datetime

class Palindrome:
    def __init__(self, last_service_date, warning_light_on):
        self.__current_date = datetime.today().date()
        self.__car = CarFactory.create_palindrome(self.__current_date, last_service_date, warning_light_on)   

    def needs_service(self):
        return self.__car.needs_service()