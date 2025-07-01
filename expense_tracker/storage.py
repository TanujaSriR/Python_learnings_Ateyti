import csv
import os
from expense import Expense

FILE_PATH = 'data/expenses.csv'

def initialize_storage():
    os.makedirs('data', exist_ok=True)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

def save_expense(expense):
    with open(FILE_PATH, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(expense.to_list())

def load_expenses():
    expenses = []
    with open(FILE_PATH, 'r') as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            expenses.append(Expense.from_list(row))
    return expenses
