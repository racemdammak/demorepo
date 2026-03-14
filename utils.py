def normalize_priority(priority):
    """
    Normalize priority values.
    Supports strings and numeric values.
    """
    if isinstance(priority, int):
        mapping = {1: "low", 2: "medium", 3: "high"}
        return mapping.get(priority, "low")

    if isinstance(priority, str):
        return priority.lower().strip()

    return "low"


def normalize_urgency(urgency):
    """
    Normalize urgency values.
    """
    if not urgency:
        return "normal"

    return urgency.lower().strip()


def format_report(data):
    """
    Format productivity report for display.
    """
    lines = []
    lines.append("Weekly Productivity Report")
    lines.append("--------------------------")

    lines.append(f"Total Tasks: {data['tasks_total']}")
    lines.append(f"Completed Tasks: {data['tasks_completed']}")
    lines.append(f"Productivity: {round(data['productivity'] * 100, 2)}%")

    return "\n".join(lines)