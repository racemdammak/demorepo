def format_report(data):
    lines = []
    lines.append("Weekly Productivity Report")
    lines.append("--------------------------")

    lines.append(f"Total Tasks: {data['tasks_total']}")
    lines.append(f"Productivity: {round(data['productivity'] * 100, 2)}%")

    return "\n".join(lines)


def normalize_priority(priority):
    return priority.lower().strip()