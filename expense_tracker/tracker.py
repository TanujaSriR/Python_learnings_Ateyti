from expense import Expense
from storage import save_expense, load_expenses
from datetime import datetime
from collections import defaultdict

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ") or datetime.now().strftime('%Y-%m-%d')
    category = input("Enter category (Food, Transport, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    exp = Expense(date, category, amount, description)
    save_expense(exp)
    print("Expense added!\n")

def view_expenses():
    expenses = load_expenses()
    print("\n All Expenses:")
    for exp in expenses:
        print(f"{exp.date} | {exp.category} | ₹{exp.amount} | {exp.description}")

def category_summary():
    expenses = load_expenses()
    summary = defaultdict(float)
    for exp in expenses:
        summary[exp.category] += exp.amount
    print("\n Total spent per category:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt:.2f}")
