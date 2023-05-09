from abc import ABC, abstractmethod
class create_car(ABC):
    def __init__(self,engine,battery):
        self.engine=engine
        self.battery=battery

    def check_service(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced()