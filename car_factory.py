from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from car import Car

class CarFactory():
    """
    Factory to create car objects. 
    Factory does not maintain any of the instances it creates
    """

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        return Car(CapuletEngine(current_mileage, last_service_mileage), 
                   SpindlerBattery(last_service_date, current_date),
                   OctoprimeTire(tire_wear_sensors))

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensors):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), 
                   SpindlerBattery(last_service_date, current_date),
                   OctoprimeTire(tire_wear_sensors))

    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear_sensors):
        return Car(SternmanEngine(warning_light_on), 
                   SpindlerBattery(last_service_date, current_date),
                   OctoprimeTire(tire_wear_sensors))

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), 
                   NubbinBattery(last_service_date, current_date),
                   CarriganTire(tire_wear_sensors))

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage), 
                   NubbinBattery(last_service_date, current_date),
                   CarriganTire(tire_wear_sensors))
