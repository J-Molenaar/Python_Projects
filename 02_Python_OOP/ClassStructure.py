Class examples:
Includes Attributes and Methods


class User(object):
    def __init__(self, name, email):  # __init__ is called EVERY TIME a new object is created. init = initialize
        self.name = name  # These are attributes and are the parameters passed into it
        self.email = email
        self.logged = True

    def login(self):  # this is a method created to help the user log in
        self.logged = True
        print self.name + " is logged in."
        return self

    def logout(self):  # this is a method created to help user log out
        self.logged = False
        print self.name + " is not logged in"
        return self

    def show(self):  # print name and email of the calling instance
        print "My name is {}. You can email me at {}".format(self.name, self.email)
        return self


Inheritance  examples:
When child classes are created we use childname(parentname) where it is
implied that parent methods and attributes are inherited(implicit
                                                         inheritance)


class Vehicle(object):  # Vehicle is the parent class
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0

    def drive(self, miles):
        self.miles += miles
        return self

    def reverse(self, miles):
        self.mile -= miles
        return self


class Bike(Vehicle):  # Bike is a child class of Vehicle, parent methods and attributes are implicitly inherited

    def vehicle_type(self):
        return "Bike"


class Car(Vehicle):  # Car is a child class of Vehicle, parent methods and attributes are implicitly inherited
    def set_wheels(self):
        self.wheels = 4
        return self


class Airplane(Vehicle):  # Airplane is a child class of Vehicle
    def fly(self, miles):
        self.mileage += miles
        return self


v = Vehicle(4, 8, "dodge", "minivan")
print v.make
b = Bike(2, 1, "Schwinn", "Paramount")
print b.vehicle_type()
c = Car(8, 5, "Toyota", "Matrix")
c.set_wheels()
print c.wheels
a = Airplane(22, 853, "Airbus", "A380")
a.fly(580)
print a.mileage

SUPER example:
    # Human.py which is stored in a the same file as a module where Human is a parent class.
from human import Human


class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence

    def heal(self):
        self.health += 10


class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth

    def steal(self):
        self.stealth += 5


class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()  # use super to call the Human __init__ method
        self.strength = 10               # every Samurai starts off with 10 strength

    def sacrifice(self):
        self.health -= 5
