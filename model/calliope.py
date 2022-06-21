from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from datetime import datetime


class Calliope():
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, datetime.today().date())

    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()