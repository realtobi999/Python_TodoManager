from pathlib import Path
from .file_task_parser import parse_tasks


def run(task_file_path: str):
    # parse tasks from a file
    tasks = parse_tasks(file_path=Path(task_file_path))
