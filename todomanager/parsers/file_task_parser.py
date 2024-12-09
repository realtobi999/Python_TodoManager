from pathlib import Path
from typing import List
from datetime import datetime
from todomanager.entities.task import Task, TaskPriority


def parse_tasks(file_path: Path) -> List[Task]:
    """
    Parses tasks from a provided text file, using the following format:

    {ID};{NAME};{PRIORITY};{DEADLINE-YYYY-MM-DD};{STATUS}

    Args:
        file_path (Path): Path to the text file from where  will  the  tasks  be
        parsed.

    Raises:
        FileNotFoundError: Raised when the specified file path is  invalid,  the
        file does not exist, or cannot be accessed. ValueError: Raised when  the
        tasks in the file are improperly formatted or contain invalid data.

    Returns:
        List[Task]: A list of tasks parsed from the provided text file.
    """
    with file_path.open("r", encoding="utf-8") as file:
        task_lines = [line.strip() for line in file.readlines()]

    tasks = []
    task_ids = set()  # Set ensures that task IDs are unique.

    for line_number, task_line in enumerate(task_lines):
        fields = task_line.split(";")

        try:
            task = map_task_from_fields(fields)
        except ValueError as e:
            raise ValueError(f"Invalid format on line {line_number + 1}: {e}") from e

        if task.id in task_ids:
            raise ValueError(f"Duplicate ID found: {task.id} on line {line_number + 1}")

        task_ids.add(task.id)
        tasks.append(task)

    return tasks


def map_task_from_fields(fields: List[str]) -> Task:
    """
    Validates a list of task fields and creates a new task.

    Args:
        fields (List[str]): A list containing exactly  5  strings,  representing
        task fields: {ID}, {NAME}, {PRIORITY}, {DEADLINE-YYYY-MM-DD}, {STATUS}.

    Raises:
        ValueError: Raised when the provided fields are incorrect, or of invalid
        value.

    Returns:
        Task: A validaded task created from the provided fields.
    """
    # Ensure the correct number of fields is provided.
    if len(fields) != 5:
        raise ValueError(f"Line must contain exactly 5 fields, but found {len(fields)} fields.")

    # Parse and validate the task ID.
    try:
        task_id = int(fields[0])
    except ValueError as e:
        raise ValueError(f"Invalid ID '{fields[0]}': Must be an integer.") from e

    if task_id <= 0:
        raise ValueError(f"Invalid ID '{fields[0]}': Must be greater than zero.")

    # Parse and validate the task priority.
    priority_parse_success, task_priority = TaskPriority.try_parse(fields[2])
    if not priority_parse_success:
        valid_priorities = ", ".join(f"{priority.name} ({priority.value})" for priority in TaskPriority)
        raise ValueError(f"Invalid priority '{fields[2]}': Must be one of {valid_priorities}.")

    # Parse and validate the deadline if provided.
    try:
        task_deadline = datetime.strptime(fields[3], "%Y-%m-%d") if fields[3] else None
    except ValueError as e:
        raise ValueError(f"Invalid deadline '{fields[3]}': Expected format: YYYY-MM-DD.") from e

    # Validate the status field, ensuring it matches expected values.
    task_status = fields[4].strip().lower()
    if task_status not in ["ano", "ne"]:
        raise ValueError(f"Invalid status '{fields[4]}': Must be 'ANO' or 'NE' (case-insensitive).")

    # Return a validated Task object.
    return Task(
        id=task_id,
        name=fields[1].strip(),
        priority=task_priority,
        deadline=task_deadline,
        status=task_status == "ano",
    )
