from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear_sensor_array):
        self.__wear_sensor_array = wear_sensor_array

    def needs_service(self):
        return max(self.__wear_sensor_array)>=0.9
           