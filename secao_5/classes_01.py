# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Car():

    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, engine):
        self._engine = engine.name
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer.name


class Engine():
    
    def __init__(self, name):
        self.name = name

class Manufacturer():

    def __init__(self, name):
        self.name = name

engine1, engine2 = Engine('Engine 1'), Engine('Engine 2')
manufacturer1, manufacturer2 = Manufacturer('VolksWagen'), Manufacturer('Jeep')
car1 = Car('Gol 1.0')
car2 = Car('Renegade')

car1.engine = engine1
car1.manufacturer = manufacturer1

car2.engine = engine2
car2.manufacturer = manufacturer2

print(car1.name, car1.manufacturer, car1.engine)
print(car2.name, car2.manufacturer, car2.engine)