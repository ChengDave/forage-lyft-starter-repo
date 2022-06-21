from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery
from datetime import datetime


class Thovex:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(last_service_date, datetime.today().date())

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()