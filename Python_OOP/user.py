class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    def login(self):
        self.loggeed = True
        print(self.name + "is logged in.")
        return self
    def logout(self):
        self.logged = Falseprint(self.name + "is not logged in.")
    def show(self):
        print(f"My name is {self.name}. You can email me at {self.email}")
        return self

user1 = User("Kevin Camp", "kcamp4632@yahoo.com")
user1.show()
