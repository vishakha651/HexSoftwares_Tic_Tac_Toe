import json
import os

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description, 0) + amount
        self.save_expenses()
        print(f"Added expense: {description} - ${amount:.2f}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("Expenses:")
        for description, amount in self.expenses.items():
            print(f"{description}: ${amount:.2f}")

    def delete_expense(self, description):
        if description in self.expenses:
            del self.expenses[description]
            self.save_expenses()
            print(f"Deleted expense: {description}")
        else:
            print(f"No expense found for: {description}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(description, amount)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            description = input("Enter expense description to delete: ")
            tracker.delete_expense(description)
        elif choice == '4':
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()