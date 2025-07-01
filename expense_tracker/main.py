from tracker import add_expense, view_expenses, category_summary
from storage import initialize_storage

def menu():
    print("\n Personal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Category Summary")
    print("4. Exit")

if __name__ == "__main__":
    initialize_storage()
    while True:
        menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            print(" Goodbye!")
            break
        else:
            print("Invalid choice.")
