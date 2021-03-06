class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        if (self.miles > 0):
            self.miles -= 5
        else:
            print "You have no where left to go..."
        return self


bike1 = Bike(150, "30 mph")
bike2 = Bike(200, "45 mph")
bike3 = Bike(250, "60 mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
