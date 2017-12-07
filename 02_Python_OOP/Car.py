class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.max_speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = self.tax()

    def tax(self):
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        return self.tax

    def displayInfo(self):
        print ("Price: ${}\nSpeed: {} mph\nFuel: {} mpg\nMileage: {} miles\nTax: {}").format(
            self.price, self.max_speed, self.fuel, self.mileage, self.tax)


Car(2000, "35mph", "Full", "15mpg").displayInfo()
Car(2000, "5mph", "Not Full", "105mpg").displayInfo()
Car(2000, "15mph", "Kind of Full", "95mpg").displayInfo()
Car(2000, "25mph", "Full", "25mpg").displayInfo()
Car(2000, "45mph", "Empty", "25mpg").displayInfo()
Car(2000000, "35mph", "Empty", "15mpg").displayInfo()
