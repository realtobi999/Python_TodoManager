from pathlib import Path
from typing import List
from todomanager.commands._commands_editing import add_task_command, complete_task_command, edit_task_command, remove_task_command
from todomanager.commands._commands_listing import list_tasks, list_tasks_with_filtering
from todomanager.console.console import ConsoleManager
from todomanager.entities.command import Command
from todomanager.entities.task import Task
from todomanager.savers.file_task_saver import save_tasks


class CommandTaskService:
    @staticmethod
    def add_task(tasks: List[Task]) -> List[Task]:
        return add_task_command(tasks)

    @staticmethod
    def remove_task(tasks: List[Task]) -> List[Task]:
        return remove_task_command(tasks)

    @staticmethod
    def complete_task(tasks: List[Task]) -> List[Task]:
        return complete_task_command(tasks)

    @staticmethod
    def edit_task(tasks: List[Task]) -> List[Task]:
        return edit_task_command(tasks)

    @staticmethod
    def list_tasks(tasks: List[Task], filtering: bool = False, clear_console: bool = False) -> None:
        if filtering:
            list_tasks_with_filtering(tasks)
        else:
            list_tasks(tasks, clear_console=clear_console)


def run_command(selected_command: Command, tasks: List[Task], tasks_file_path: Path) -> None:
    console = ConsoleManager.get_instance()

    if selected_command == Command.ADD:
        tasks = CommandTaskService.add_task(tasks)

    elif selected_command == Command.LIST:
        ConsoleManager.print_divider(text="Zobrazení úkolů")
        filter_choice = ConsoleManager.input_int(text="[reset]Chcete filtrovat? (0/1): ", conditions=[lambda n: n == 1 or n == 0])

        CommandTaskService.list_tasks(tasks, filtering=True if filter_choice == 1 else False, clear_console=True)

    elif selected_command == Command.REMOVE:
        tasks = CommandTaskService.remove_task(tasks)

    elif selected_command == Command.COMPLETE:
        tasks = CommandTaskService.complete_task(tasks)

    elif selected_command == Command.EDIT:
        tasks = CommandTaskService.edit_task(tasks)

    elif selected_command == Command.SAVE:
        save_tasks(file_path=Path(tasks_file_path), tasks=tasks)
        console.print("\nÚkoly byly uloženy.", style="bold green")
