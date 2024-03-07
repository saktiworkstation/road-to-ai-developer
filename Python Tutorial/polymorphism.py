print('- class polymorphism')
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('driving')

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Sailing')

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Flying')

car1 = Car('Ford', 'Mustang')
boat1 = Boat('Ibiza', 'touring 20')
plane1 = Plane('Boeing', '747')

for x in (car1, boat1, plane1):
    x.move()

print('- Inheritance Class Polymorphism')
class Veicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Moving')

class Car(Veicle):
    pass

class Boat(Veicle):
    def move(self):
        print('Sailing')

class Plane(Veicle):
    def move(self):
        print('Flying')

car1 = Car('Ford', 'Mustang')
boat1 = Boat('Ibiza', 'touring 20')
plane1 = Plane('Boeing', '747')

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()