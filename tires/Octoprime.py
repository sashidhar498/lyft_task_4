class octoprime:
    def __init__(self,tires):
        self.tires=tires
    def tire_should_be_serviced(self):
        return sum(self.tires)>=3