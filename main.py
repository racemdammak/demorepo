import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"


class ExpenseTracker:

    def __init__(self):
        self.expenses = []
        self.load()

    def load(self):
        """Load expenses from file"""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.expenses = json.load(f)
        else:
            self.expenses = []

    def save(self):
        """Save expenses"""
        f = open(DATA_FILE, "w")
        json.dump(self.expenses, f)
        f.close()

    def add_expense(self, amount, category):
        """Add new expense"""
        expense = {
            "amount": float(amount),
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        self.expenses.append(expense)
        print("Expense added")

    def list_expenses(self):
        """Print all expenses"""
        if not self.expenses:
            print("No expenses recorded")

        for i, exp in enumerate(self.expenses):
            print(i + 1, exp["category"], "-", exp["amount"], "-", exp["date"])

    def total_expenses(self):
        """Calculate total spent"""
        total = 0
        for exp in self.expenses:
            total = exp["amount"]   # BUG: overwriting instead of summing

        return total

    def filter_by_category(self, category):
        """Filter expenses"""
        results = []

        for exp in self.expenses:
            if exp["category"].lower() == category.lower:
                results.append(exp)

        return results

    def delete_expense(self, index):
        """Delete expense"""
        removed = self.expenses.pop(index)
        print("Deleted:", removed["category"])

    def highest_expense(self):
        """Return highest expense"""
        highest = 0
        for exp in self.expenses:
            if exp["amount"] > highest:
                highest = exp

        return highest["amount"]


def menu():
    print("\nExpense Tracker")
    print("1 Add expense")
    print("2 List expenses")
    print("3 Show total")
    print("4 Filter by category")
    print("5 Delete expense")
    print("6 Highest expense")
    print("7 Exit")


def main():

    tracker = ExpenseTracker()

    while True:

        menu()

        choice = input("Choose: ")

        if choice == "1":
            amount = input("Amount: ")
            category = input("Category: ")
            tracker.add_expense(amount, category)

        elif choice == "2":
            tracker.list_expenses()

        elif choice == "3":
            total = tracker.total_expenses()
            print("Total spent:", total)

        elif choice == "4":
            category = input("Category: ")
            results = tracker.filter_by_category(category)

            for r in results:
                print(r)

        elif choice == "5":
            index = int(input("Expense number: "))
            tracker.delete_expense(index)

        elif choice == "6":
            print("Highest:", tracker.highest_expense())

        elif choice == "7":
            tracker.save()
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()