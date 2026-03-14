from analytics import generate_weekly_report, rank_tasks
from storage import load_tasks


def main():
    tasks = load_tasks("tasks.json")

    if not tasks:
        print("No tasks found.")
        return

    print(generate_weekly_report(tasks))

    print("\nTask Ranking:")
    ranking = rank_tasks(tasks)

    for title, score in ranking:
        print(f"{title} -> {score}")


if __name__ == "__main__":
    main()