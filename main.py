from notes_manager import NotesManager


def main():
    manager = NotesManager()

    while True:
        print("\n--- Notes Manager ---")
        print("1. Add note")
        print("2. View notes")
        print("3. Delete note")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            content = input("Enter note: ")
            manager.add_note(content)

        elif choice == "2":
            notes = manager.get_notes()
            if not notes:
                print("No notes available.")
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note}")

        elif choice == "3":
            notes = manager.get_notes()
            if not notes:
                print("No notes to delete.")
                continue

            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

            index = int(input("Enter note number to delete: ")) - 1
            manager.delete_note(index)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()