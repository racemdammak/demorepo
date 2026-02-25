from task_manager import TaskManager

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        status = "✔" if task.completed else "✘"
        print(f"{i}. [{status}] {task.title} (Priority: {task.priority})")

def main():
    manager = TaskManager()

    while True:
        print("\n=== TODO APP ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Mark Completed")
        print("5. Search Task")
        print("6. Sort by Priority")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            priority = int(input("Priority (1=High, 5=Low): "))
            manager.add_task(title, desc, priority)

        elif choice == "2":
            display_tasks(manager.list_tasks())

        elif choice == "3":
            display_tasks(manager.list_tasks())
            index = int(input("Index to delete: "))
            manager.delete_task(index)

        elif choice == "4":
            display_tasks(manager.list_tasks())
            index = int(input("Index to mark complete: "))
            manager.mark_completed(index)

        elif choice == "5":
            keyword = input("Search keyword: ")
            results = manager.search_tasks(keyword)
            display_tasks(results)

        elif choice == "6":
            manager.sort_by_priority()
            print("Tasks sorted by priority.")

        elif choice == "7":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()