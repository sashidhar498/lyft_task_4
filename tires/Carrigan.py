class carrigan:
    def __init__(self,tires):
        self.tires=tires
    def tire_should_be_serviced(self):
        return any(value>=0.9 for value in self.tires)
