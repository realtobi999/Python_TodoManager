from pathlib import Path
from typing import Optional

from todomanager.savers.file_task_saver import save_tasks
from .entities.commands import Command, get_command_from_user, run_command
from .commands.commands_listing import list_tasks
from .parsers.file_task_parser import parse_tasks
from .console.console import ConsoleManager, print_intro_ascii_logo, print_divider


def run(tasks_file_path: str) -> Optional[int]:
    console = ConsoleManager.get_instance()
    # parse tasks
    try:
        tasks = parse_tasks(file_path=Path(tasks_file_path))
    except Exception as e:
        raise Exception("Chyba během načítání úkolů.") from e

    # start the application and list tasks parsed from the file
    try:
        print_intro_ascii_logo()

        print_divider(text="Aktuální seznam úkolů")
        list_tasks(tasks)
    except Exception as e:
        raise Exception("Chyba během startování aplikace.") from e

    # handle commands inputs
    while True:
        try:
            selected_command = get_command_from_user()

            if selected_command == Command.EXIT:
                save_tasks(file_path=Path(tasks_file_path), tasks=tasks)

                console.print("Úkoly byly uloženy. Ukončuji aplikaci.")
                break

            elif selected_command == Command.SAVE:
                save_tasks(file_path=Path(tasks_file_path), tasks=tasks)
                console.print("Úkoly byly uloženy.")

            run_command(selected_command, tasks)
        except Exception as e:
            raise Exception("Chyba během zpracování příkazů.") from e

    # return 0 if everything went as planned
    return 0
