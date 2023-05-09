from abc import ABC
from datetime import datetime

class battery(ABC):
    def __init__(self,current_date,last_service_date):
        self.last_service_date = last_service_date
        self.current_date=current_date
    def check(self,service_threshold_date):
        return service_threshold_date < datetime.today().date()
