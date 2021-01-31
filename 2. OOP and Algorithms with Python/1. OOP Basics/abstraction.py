class WashingMachine:

    def __init__(self):
        pass

    def wash(self, temperature='caliente'):
        self._filling_tank_with_water(temperature)
        self._add_soap()
        self._lavar()
        self._centrifugar()

    def _filling_tank_with_water(self, temperature):
        print(f'Llenando el tanque con agua a {temperature}')

    def _add_soap(self):
        print('Añadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    lavadora = WashingMachine()
    lavadora.wash()