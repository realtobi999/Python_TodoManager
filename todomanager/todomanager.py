from pathlib import Path
from typing import Optional
from .commands.commands import COMMANDS, get_command_from_user, handle_selected_command
from .commands.commands_listing import list_tasks
from .parsers.file_task_parser import parse_tasks
from .console.console import ConsoleManager, print_ascii_logo, print_divider


def run(task_file_path: str) -> Optional[int]:
    print_ascii_logo()

    # parse tasks
    try:
        tasks = parse_tasks(file_path=Path(task_file_path))
    except Exception as e:
        raise Exception("Chyba během načítání úkolů.") from e

    # list all tasks
    list_tasks(tasks)
    print_divider(text="Aktuální seznam úkolů")

    # handle commands inputs
    while True:
        try:
            selected_command = get_command_from_user()

            if selected_command == COMMANDS[-1]:
                console = ConsoleManager.get_instance()

                console.print("Úkoly byly uloženy. Ukončuji aplikaci.")
                break
            else:
                handle_selected_command(selected_command, tasks)
        except Exception as e:
            raise Exception("Chyba během zpracování příkazů.") from e

    # return 0 if everything went as planned
    return 0
