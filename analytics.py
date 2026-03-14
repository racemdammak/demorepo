from utils import format_report, normalize_priority

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

    priority = normalize_priority(task["priority"])

    if priority == "high":
        score += 5
    elif priority == "medium":
        score += 3
    else:
        score += 1

    if task["done"]:
        score += 2

    return score


def rank_tasks(tasks):
    scored = []

    for task in tasks:

        if isinstance(task["priority"], int):
            mapping = {1: "low", 2: "medium", 3: "high"}
            task["priority"] = mapping.get(task["priority"], "low")

        score = calculate_task_score(task)

        if task.get("urgency") == "critical":
            score += 5

        scored.append((task["title"], score))

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored