from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from datetime import datetime


class Rorschach:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(last_service_date, datetime.today().date())

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()