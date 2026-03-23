

rates = {"KGS": 1,"USD": 89,"EUR": 96,"RUB": 1.2}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def convert_to_kgs(self):
        rate = rates[self.currency]
        return self.amount * rate
    def __add__(self, other):
        kgs = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(kgs, "kgs")
    def __sub__(self, other):
        kgs = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(kgs, "kgs")
    def __mul__(self, number):
        return Money(self.amount * number, self.currency)
    def __truediv__(self, number):
        return Money(self.amount / number, self.currency)
    def __str__(self):
        return f'{self.amount} {self.currency}'


