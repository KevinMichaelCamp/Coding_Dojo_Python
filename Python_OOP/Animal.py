# Animal Assignment


class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health += 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print(self.name + "'s health: " + str(self.health))


# Test Case 1
animal1 = Animal("Bobo")
animal1.walk().run().displayHealth()

# Dog


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self


# Test Case 2
dog1 = Dog("Spot")
dog1.walk().walk().walk().run().run().pet().displayHealth()

# Dragon


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print("I am a Dragon")


dragon1 = Dragon("Puff")
dragon1.fly().displayHealth()
