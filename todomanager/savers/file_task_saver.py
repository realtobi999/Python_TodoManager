from pathlib import Path
from typing import List
from todomanager.entities.task import Task


def save_tasks(file_path: Path, tasks: List[Task]) -> None:
    """
    Saves all provided tasks to a provided text file,  using  the
    following format:

    {ID};{NAME};{PRIORITY};{DEADLINE-YYYY-MM-DD};{STATUS}

    Args:
        file_path (Path): Path to the text file where  the  tasks
        will be stored. tasks (List[Task]): Tasks  to  save  into
        the text file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        for task in tasks:
            task_data = [
                str(task.id),
                task.name,
                task.priority.value,
                task.deadline.strftime("%Y-%m-%d") if task.deadline else "",
                "Ano" if task.status else "Ne",
            ]
            file.write(";".join(task_data) + "\n")
