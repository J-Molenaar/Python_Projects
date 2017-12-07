
class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        print "Walking"
        self.health -= 1
        return self

    def run(self):
        print "Running"
        self.health -= 5
        return self

    def displayhealth(self):
        print self.name
        print "Health level at:", self.health
        return self


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        print "Petting"
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        print "Flying"
        self.health -= 10
        return self

    def displayhealth(self):
        print self.name
        print "This is a dragon!", self.health
        return self


animal1 = Animal("Yuki")
animal1.walk().walk().walk().run().run().displayhealth()
animal2 = Dog("Blue")
animal2.walk().walk().walk().run().run().pet().displayhealth()
animal3 = Dragon("Falgore")
animal3.walk().walk().walk().run().run().fly().fly().displayhealth()

animal4 = Animal  # testing cannot call pet() or fly()
animal4.pet().fly().fly().displayhealth()
