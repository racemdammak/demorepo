from storage import load_expenses, save_expenses


class ExpenseManager:
    def __init__(self):
        self.expenses = load_expenses()

    def add_expense(self, description, amount):
        # BUG: Allows negative values
        expense = {
            "description": description,
            "amount": amount
        }
        self.expenses.append(expense)
        save_expenses(self.expenses)

    def list_expenses(self):
        return self.expenses

    def calculate_total(self):
        # BUG: Wrong calculation (concatenates instead of sums if amount is string)
        total = 0
        for expense in self.expenses:
            total += expense["amount"]
        return total