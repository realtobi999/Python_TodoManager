from enum import Enum
from typing import Optional, Tuple
from todomanager.console.console import ConsoleManager


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


def get_command_from_user() -> Command:
    console = ConsoleManager.get_instance()
    ConsoleManager.print_divider(text="Příkazový řádek")

    available_commands = [command.value for command in Command]
    console.print(f"Příkazy: {", ".join(f"'{command}'" for command in available_commands)}\n")

    command = Command(
        ConsoleManager.input_string(
            text="Zadejte příkaz: ",
            error_message="Neznámý příkaz, zkuste to prosím znovu.",
            conditions=[lambda command: command.strip() in available_commands],
        ).strip()
    )

    return command
