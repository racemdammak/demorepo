from utils import format_report

def calculate_productivity(tasks):
    completed = [t for t in tasks if t["done"]]
    total = len(tasks)

    if total == 0:
        return 0

    return len(completed) / total


def generate_weekly_report(tasks):
    productivity = calculate_productivity(tasks)

    report = {
        "tasks_total": len(tasks),
        "productivity": productivity
    }

    return format_report(report)


def calculate_task_score(task):
    score = 0

    if task["priority"] == "high":
        score += 5
    elif task["priority"] == "medium":
        score += 3
    else:
        score += 1

    if task["done"]:
        score += 2

    return score