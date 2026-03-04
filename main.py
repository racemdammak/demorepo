from expense_manager import ExpenseManager


def main():
    manager = ExpenseManager()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            description = input("Description: ")
            amount = input("Amount: ")  # BUG: Not converting to float
            manager.add_expense(description, amount)
            print("Expense added.")

        elif choice == "2":
            expenses = manager.list_expenses()
            for e in expenses:
                print(f"{e['description']} - {e['amount']}")

        elif choice == "3":
            print("Total:", manager.calculate_total())

        elif choice == "4":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()