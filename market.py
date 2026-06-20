import random

class Market:
    def __init__(self):
        self.price = 100

    def tick(self):
        change = random.uniform(-2, 2)

        self.price += change

        if self.price < 1:
            self.price = 1

        return round(self.price, 2)
