from datetime import datetime

class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_list(self):
        return [self.date, self.category, str(self.amount), self.description]

    @staticmethod
    def from_list(data):
        return Expense(data[0], data[1], float(data[2]), data[3])
