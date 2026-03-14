from utils import format_report, normalize_priority, normalize_urgency


def calculate_productivity(tasks):
    """
    Calculate completion ratio.
    """
    total = len(tasks)

    if total == 0:
        return 0

    completed = [t for t in tasks if t.get("done")]

    return len(completed) / total


def calculate_task_score(task):
    """
    Score a task based on priority, completion, and urgency.
    """
    score = 0

    priority = normalize_priority(task.get("priority"))
    urgency = normalize_urgency(task.get("urgency"))

    if priority == "high":
        score += 5
    elif priority == "medium":
        score += 3
    else:
        score += 1

    if task.get("done"):
        score += 2

    if urgency == "critical":
        score += 5
    elif urgency == "high":
        score += 3

    return score


def rank_tasks(tasks):
    """
    Rank tasks by computed score.
    """
    scored = []

    for task in tasks:
        score = calculate_task_score(task)
        scored.append((task["title"], score))

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored


def generate_weekly_report(tasks):
    """
    Generate productivity report.
    """
    productivity = calculate_productivity(tasks)

    completed = len([t for t in tasks if t.get("done")])

    report = {
        "tasks_total": len(tasks),
        "tasks_completed": completed,
        "productivity": productivity
    }

    return format_report(report)