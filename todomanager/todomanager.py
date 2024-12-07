import traceback
from pathlib import Path
from typing import Optional
from todomanager.commands.command_manager import CommandTaskService, run_command
from todomanager.console.console import ConsoleManager
from todomanager.entities.command import Command, get_command_from_user
from todomanager.parsers.file_task_parser import parse_tasks
from todomanager.savers.file_task_saver import save_tasks


def run(tasks_file_path: str) -> Optional[int]:
    console = ConsoleManager.get_instance()
    console.clear()

    try:
        # parse tasks
        try:
            tasks = parse_tasks(file_path=Path(tasks_file_path))
        except Exception as e:
            raise Exception("Chyba během načítání úkolů.") from e

        # start the application and list tasks parsed from the file
        try:
            ConsoleManager.print_intro_ascii_logo()
            ConsoleManager.print_divider(text="Aktuální seznam úkolů")
            CommandTaskService.list_tasks(tasks)
        except Exception as e:
            raise Exception("Chyba během startování aplikace.") from e

        # handle commands inputs
        while True:
            try:
                selected_command = get_command_from_user()

                if selected_command == Command.EXIT:
                    save_tasks(file_path=Path(tasks_file_path), tasks=tasks)

                    console.print("Úkoly byly uloženy. Ukončuji aplikaci.")

                    # return 0 if everything went as planned
                    return 0
                else:
                    run_command(selected_command, tasks, tasks_file_path)

            except Exception as e:
                raise Exception("Chyba během zpracování příkazů.") from e
    except Exception as e:
        ConsoleManager.print_error_ascii_logo()
        console.print(f"Chyba v systému: {e}", style="bold red")

        # ask for debug mode
        console.print("\n[reset]DEBUG MODE? (0/1)")
        should_debug = ConsoleManager.input_int(
            text="=> ",
            error_message="Neplatný vstup.",
            conditions=[lambda n: n == 0 or n == 1],
        )
        if should_debug == 1:
            traceback.print_exception(e.__cause__)

        # ask for restart of the application
        console.print("\n[reset]Chcete zkusit restartovat aplikaci? (0/1)")
        should_continue = ConsoleManager.input_int(
            text="=> ",
            error_message="Neplatný vstup.",
            conditions=[lambda n: n == 0 or n == 1],
        )
        if should_continue == 1:
            return run(tasks_file_path)
        if should_continue == 0:
            return 0
