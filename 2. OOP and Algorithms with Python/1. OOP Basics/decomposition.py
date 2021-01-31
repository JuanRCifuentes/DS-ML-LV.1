class Car:

    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.state = 'resting'
        self._engine = Engine(4)

    def refuel(self, amount):
        self._engine.inyect_gas(amount)

class Engine:

    def __init__(self, cylinders, kind='gas'):
        self.cylinders = cylinders
        self.kind = kind
        self._temperature = 0
        self.fuel = 0

    def inyect_gas(self, amount_of_gas):
        self.fuel += amount_of_gas