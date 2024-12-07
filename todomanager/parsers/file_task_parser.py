from pathlib import Path
from typing import Dict, List
from datetime import datetime
from todomanager.entities.task import Task, TaskPriority


def parse_tasks(file_path: Path) -> List[Task]:
    with file_path.open("r", encoding="utf-8") as file:
        task_lines = [line.strip() for line in file.readlines()]

    tasks = []
    task_ids = set()  # set because it handles uniqueness

    for line_number, task_line in enumerate(task_lines):
        fields = task_line.split(";")

        try:
            task = map_task_from_fields(fields)
        except ValueError as e:
            raise ValueError(f"Invalid format on line {line_number + 1}: {e}") from e

        # validate that each task has a unique id
        if task.Id in task_ids:
            raise ValueError(f"Duplicate ID found: {task.Id} on line {line_number + 1}")

        task_ids.add(task.Id)
        tasks.append(task)

    return tasks


def map_task_from_fields(fields: List[str]) -> Task:
    # validate correct task format
    if len(fields) != 5:
        raise ValueError(f"Line must contain exactly 5 fields, but found {len(fields)} fields.")

    # parse and validate ID
    try:
        task_id = int(fields[0])
    except ValueError as e:
        raise ValueError(f"Invalid ID '{fields[0]}': Must be an integer.") from e

    if task_id <= 0:
        raise ValueError(f"Invalid ID '{fields[0]}: Must be bigger than zero.'")

    # parse and validate priority
    priority_parse_success, task_priority = TaskPriority.try_parse(fields[2])
    if not priority_parse_success:
        valid_priorities = ", ".join(f"{priority.name} ({priority.value})" for priority in TaskPriority)
        raise ValueError(f"Invalid priority '{fields[2]}': Must be one of {valid_priorities}.")

    # parse and validate deadline
    try:
        if fields[3]:
            task_deadline = datetime.strptime(fields[3], "%Y-%m-%d")
        else:
            task_deadline = None
    except ValueError as e:
        raise ValueError(f"Invalid deadline '{fields[3]}': Unable to parse the date. Expected format: YYYY-MM-DD.") from e

    # parse and validate status
    task_status = fields[4].strip().lower()
    if task_status not in ["ano", "ne"]:
        raise ValueError(f"Invalid status '{fields[4]}': Must be 'ANO' or 'NE' (case-insensitive).")

    return Task(
        Id=task_id,
        Name=fields[1].strip(),
        Priority=task_priority,
        Deadline=task_deadline,
        Status=task_status == "ano",
    )
