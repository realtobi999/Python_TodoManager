from typing import List, Optional, Tuple
from enum import Enum
from todomanager.commands.commands_editing import (
    add_task_command,
    complete_task_command,
    edit_task_command,
    remove_task_command,
)
from todomanager.commands.commands_listing import list_tasks, list_tasks_command
from todomanager.console.console import ConsoleManager, print_divider
from todomanager.entities.task import Task


class Command(Enum):
    ADD = "add"
    LIST = "list"
    REMOVE = "remove"
    COMPLETE = "complete"
    EDIT = "edit"
    SAVE = "save"
    EXIT = "exit"

    @classmethod
    def try_parse(cls, value: str) -> Tuple[bool, Optional["Command"]]:
        for command in cls:
            if command.value == value:
                return True, command
        return False, None


def run_command(selected_command: Command, tasks: List[Task]) -> None:
    console = ConsoleManager.get_instance()

    if selected_command == Command.ADD:
        tasks = add_task_command(tasks)

    elif selected_command == Command.LIST:
        while True:
            filter_choice = console.input("[reset]Chcete filtrovat? (0/1): ").strip()

            if filter_choice == "1":
                list_tasks_command(tasks)
                return
            elif filter_choice == "0":
                list_tasks(tasks)
                return
            else:
                console.print("Neplatný vstup, prosím zkuste to znovu.", style="italic red")

    elif selected_command == Command.REMOVE:
        tasks = remove_task_command(tasks)

    elif selected_command == Command.COMPLETE:
        tasks = complete_task_command(tasks)

    elif selected_command == Command.EDIT:
        tasks = edit_task_command(tasks)


def get_command_from_user() -> Command:
    console = ConsoleManager.get_instance()

    while True:
        print_divider(text="Příkazový řádek")

        available_commands = ", ".join(f"'{command.value}'" for command in Command)
        console.print(f"Příkazy: {available_commands}\n", style="bold")

        entered_command = console.input("Zadejte příkaz: ").strip()
        is_valid_command, parsed_command = Command.try_parse(entered_command)

        if not is_valid_command:
            console.print("Neznámý příkaz, prosím zkuste to znovu.", style="italic red")
        else:
            return parsed_command
