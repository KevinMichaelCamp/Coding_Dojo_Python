# Math Dojo Assignment


class MathDojo:
    def __init__(self):
        self.value = 0

    def add(self, *num):
        for i in num:
            self.value += i
        return self

    def subtract(self, *num):
        for i in num:
            self.value -= i
        return self

    def result(self):
        print(self.value)


md = MathDojo()
md.add(2).add(2, 5, 1).subtract(3, 2).result()
