from Battery.battery import battery
from datetime import datetime

class spindler(battery):
    def __init__(self,current_date,last_service_date):
        super().__init__(current_date,last_service_date)

    def battery_should_be_serviced (self):
        service_date=self.last_service_date.replace(year=self.last_service_date.year + 2)
        return self.check(service_date)
