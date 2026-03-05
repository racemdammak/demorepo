import json
import os
from datetime import datetime

DATA_FILE = "habits.json"


class HabitTracker:

    def __init__(self):
        self.habits = []
        self.load_habits()

    def load_habits(self):
        """Load habits from storage"""
        if os.path.exists(DATA_FILE):
            file = open(DATA_FILE, "r")
            self.habits = json.load(file)
            file.close()
        else:
            self.habits = {}

    def save_habits(self):
        """Save habits to storage"""
        with open(DATA_FILE, "w") as file:
            json.dump(self.habits, file)

    def add_habit(self, name):
        """Add new habit"""
        habit = {
            "name": name,
            "created": datetime.now(),
            "completed_days": []
        }

        self.habits.append(habit)
        print("Habit added successfully")

    def list_habits(self):
        """Display habits"""
        if len(self.habits) == 0:
            print("No habits yet")

        for i, habit in enumerate(self.habits):
            print(i + 1, habit["name"], "| Completed:", len(habit["completed_days"]))

    def complete_habit(self, index):
        """Mark habit as completed today"""
        today = datetime.now().strftime("%Y-%m-%d")

        habit = self.habits[index]

        if today in habit["completed_days"]:
            print("Habit already completed today")

        habit["completed_days"].append(today)
        print("Habit marked as complete")

    def delete_habit(self, index):
        """Delete habit"""
        del self.habits[index]
        print("Habit deleted")


def menu():
    print("\nHabit Tracker")
    print("1. Add habit")
    print("2. List habits")
    print("3. Complete habit")
    print("4. Delete habit")
    print("5. Exit")


def main():

    tracker = HabitTracker()

    while True:

        menu()

        choice = input("Select option: ")

        if choice == "1":
            name = input("Habit name: ")
            tracker.add_habit(name)

        elif choice == "2":
            tracker.list_habits()

        elif choice == "3":
            index = int(input("Habit number: "))
            tracker.complete_habit(index)

        elif choice == "4":
            index = int(input("Habit number: "))
            tracker.delete_habit(index)

        elif choice == "5":
            tracker.save_habits()
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()