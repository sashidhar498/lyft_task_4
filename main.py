from Battery.nubbin import nubbin 
from Battery.spindler import spindler
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from factory import create_car
from datetime import datetime


class all_cars():
    def calliope(self,current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler(current_date, last_service_date)
        car=create_car(engine, battery)
        return car.check_service()

    def glissade(self,current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = spindler(current_date, last_service_date)
        car=create_car(engine, battery)
        return car.check_service()

    def palindrome(self,current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = spindler(current_date, last_service_date)
        car=create_car(engine, battery)
        return car.check_service()

    def rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = nubbin(current_date, last_service_date)
        car=create_car(engine, battery)
        return car.check_service()

    def thovex(self,current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin(current_date, last_service_date)
        car=create_car(engine, battery)
        return car.check_service()