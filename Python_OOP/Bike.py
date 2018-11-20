# Bike Assignment


class Bike:
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print("Bike")
        print("$" + str(self.price))
        print("Max Speed - " + self.max_speed)
        print("Mileage - " + str(self.miles) + " miles")
        return self

    def ride(self):
        print("Riding bike")
        self.miles += 10
        return self

    def reverse(self):
        print("Reversing bike")
        if self.miles > 0:
            self.miles -= 5
        return self


bike1 = Bike(200, '30mph', 0)
bike1.displayInfo()
bike1.ride().ride().ride().reverse()
bike1.displayInfo()
bike2 = Bike(275, "35mph", 0)
bike2.displayInfo()
bike2.ride().ride().reverse().reverse()
bike2.displayInfo()
bike3 = Bike(500, "40mph", 0)
bike3.displayInfo()
bike3.reverse().reverse().reverse()
bike3.displayInfo()
