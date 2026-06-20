class Portfolio:
    def __init__(self, balance=1000):
        self.initial = balance
        self.balance = balance
        self.position = 0
        self.history = []

    def buy(self, price, amount):
        cost = price * amount

        if self.balance >= cost:
            self.balance -= cost
            self.position += amount
            self.history.append(f"BUY {amount} @ {price:.2f}")
            return True

        return False

    def sell(self, price, amount):
        if self.position >= amount:
            self.balance += price * amount
            self.position -= amount
            self.history.append(f"SELL {amount} @ {price:.2f}")
            return True

        return False

    def value(self, current_price):
        return self.balance + self.position * current_price
