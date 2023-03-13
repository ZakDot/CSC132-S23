class Vehicle:
    def __init__(self, name):
        self.tires = None
        self.engine = None
        self.owner = name
        self.hasInsurance = True

    def __str__(self):
        return f"owner={self.owner}, tires={self.tires}, engine={self.engine}, insurance={self.hasInsurance}"
 

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.tires = 4
        self.engine = True

    def __str__(self):
        return "Car; "+ super().__str__()

class Cycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.tires = 2
        self.riders = None

    def __str__(self):
        return super().__str__() + f", riders={self.riders}"

class Bicycle(Cycle):
    def __init__(self, name):
        super().__init__(name)
        self.engine = False
        self.hasInsurance = False
        self.riders = 1
    
    def __str__(self):
        return "Bicycle; " + super().__str__()

class Motorcycle(Cycle):
    def __init__(self, name):
        super().__init__(name)
        self.engine = True
        self.hasInsurance = True
        self.riders = 2
    
    def __str__(self):
        return f"Motorcycle; " + super().__str__()

c1 = Car("Zak")
b1 = Bicycle("Timmy")
m1 = Motorcycle("Logan")
print(c1)
print(b1)
print(m1)