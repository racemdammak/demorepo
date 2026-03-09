from analytics import generate_weekly_report, calculate_task_score
from storage import load_tasks

def main():
    tasks = load_tasks("tasks.json")

    report = generate_weekly_report(tasks)
    print(report)

    print("\nTask Scores:")
    for task in tasks:
        score = calculate_task_score(task)
        print(task["title"], "->", score)


if __name__ == "__main__":
    main()