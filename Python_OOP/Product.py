# Product Assignment
class Product:
    def __init__(self, name, price, brand, weight, status="for sale"):
        self.name = name
        self.price = price
        self.brand = brand
        self.weight = weight
        self.status = status

    def displayInfo(self):
        print("Name: " + self.name)
        print("Price: $" + str(self.price))
        print("Brand: " + self.brand)
        print("Weight: " + self.weight)
        print("Status: " + self.status)
        return self

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        self.price = round(self.price + (self.price * tax), 2)
        return self

    def returnItem(self, reason):
        if reason == "defective":
            self.price = 0
        elif reason == "like new":
            self.status = "for sale"
        elif reason == "opened":
            self.price = round(self.price - (self.price * .2), 2)
            self.status = "for sale"
        else:
            print("Invalid Reason")
        return self


item1 = Product('Razor', 15.99, 'Bic', '.1 lbs')
item1.displayInfo()
item1.addTax(.08)
item1.displayInfo()
item1.sell()
item1.displayInfo()
item1.returnItem('opened')
item1.displayInfo()
