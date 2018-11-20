# Car Assignment


class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = "15%"
        else:
            self.tax = "12%"

    def displayAll(self):
        print("Price: " + str(self.price))
        print("Speed: " + self.speed)
        print("Fuel: " + self.fuel)
        print("Mileage: " + self.mileage)
        print("Tax: " + self.tax)
        return self


car1 = Car(15000, '120mph', 'Full', '45mpg')
car1.displayAll()
car1 = Car(7500, '100mph', 'Empty', '25mpg')
car1.displayAll()
