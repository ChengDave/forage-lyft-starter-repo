from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear_sensor_array):
        self.__wear_sensor_array = wear_sensor_array

    def needs_service(self):
        return sum(self.__wear_sensor_array)>=3
           