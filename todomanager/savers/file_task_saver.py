from pathlib import Path
from typing import List
from todomanager.console.console import ConsoleManager
from todomanager.entities.task import Task


def save_tasks(file_path: Path, tasks: List[Task]) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        for task in tasks:
            task_data = [
                str(task.Id),
                task.Name,
                task.Priority.value,
                task.Deadline.strftime("%Y-%m-%d") if task.Deadline else "",
                "Ano" if task.Status else "Ne",
            ]
            file.write(";".join(task_data) + "\n")
