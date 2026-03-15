from storage import load_notes, save_notes


class NotesManager:
    def __init__(self):
        self.notes = load_notes()

    def add_note(self, content: str) -> None:
        self.notes.append(content)
        save_notes(self.notes)
        print("Note added successfully.")

    def get_notes(self):
        return self.notes

    def delete_note(self, index: int) -> None:
        if 0 <= index < len(self.notes):
            removed = self.notes.pop(index)
            save_notes(self.notes)
            print(f"Deleted note: {removed}")
        else:
            print("Invalid note index.")