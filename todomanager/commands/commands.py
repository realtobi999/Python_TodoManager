from typing import List
from todomanager.commands.commands_listing import list_tasks, list_tasks_with_filtering
from todomanager.console.console import ConsoleManager, print_divider
from todomanager.entities.task import Task

COMMANDS = ["add", "list", "remove", "complete", "edit", "save", "exit"]


def handle_selected_command(selected_command: str, tasks: List[Task]) -> None:
    console = ConsoleManager.get_instance()

    # handle each command as a if statement
    while True:
        if selected_command == "list":
            while True:
                list_with_filter = console.input("[reset]Chcete filtrovat? (0/1): ")

                if list_with_filter == "1":
                    list_tasks_with_filtering(tasks)
                    return
                elif list_with_filter == "0":
                    list_tasks(tasks)
                    return
                else:
                    console.print("Neplatný vstup, prosím zkuste to znovu.", style="italic red")


def get_command_from_user() -> str:
    console = ConsoleManager.get_instance()

    while True:
        try:
            print_divider(text="Příkazový řádek")
            console.print(f"Příkazy: {', '.join(f"'{command}'" for command in COMMANDS)}\n", style="bold")

            selected_command = console.input("Zadejte příkaz: ")

            if not selected_command in COMMANDS:
                raise ValueError("Neznámý příkaz, prosím zkuste to znovu.")

            break
        except ValueError as e:
            console.print(e, style="italic red")

    return selected_command
