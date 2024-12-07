from typing import List
from rich.table import Table
from todomanager.console.console import ConsoleManager
from todomanager.entities.filter import Filter
from todomanager.entities.task import Task, TaskPriority


def list_tasks_with_filtering(tasks: List[Task]) -> None:
    console = ConsoleManager.get_instance()

    # prompt for the desired filter
    ConsoleManager.print_divider(text="Zobrazení úkolů - Filtrování")
    available_filters = [filter.value for filter in Filter]
    console.print(f"Hodnota pro filtrování: {", ".join(f"'{filter}'" for filter in available_filters)}\n")

    selected_filter = Filter(
        ConsoleManager.input_string(
            text="Zadejte filtr: ",
            error_message="Neznámá hodnota pro filtrování, zkuste to znovu.",
            conditions=[lambda filter: filter.strip() in available_filters],
        ).strip()
    )

    # filter by priority
    if selected_filter == Filter.Priority:
        ConsoleManager.print_divider(text="Zobrazení úkolů - Filtrování - Dle priority")
        available_priorities = [priority.value for priority in TaskPriority]
        console.print(f"Priority: {", ".join(f"'{priority}'" for priority in available_priorities)}\n")

        task_priority = TaskPriority(
            ConsoleManager.input_string(
                text="Zadejte prioritu: ",
                error_message="Neznámá hodnota pro prioritu, zkuste to znovu.",
                conditions=[lambda priority: priority.strip() in available_priorities],
            )
        )

        tasks = [task for task in tasks if task.Priority == task_priority]

    # filter by status
    elif selected_filter == Filter.Status:
        ConsoleManager.print_divider(text="Zobrazení úkolů - Filtrování - Dle stavu")
        available_statuses = ["Dokončeno", "Nedokončeno"]
        console.print(f"Statusy: {", ".join(f"'{status}'" for status in available_statuses)}\n")

        task_status = ConsoleManager.input_string("Zadejte stav: ", conditions=[lambda status: status.strip() in available_statuses]).strip()

        tasks = [task for task in tasks if task.Status == (True if task_status == "Dokončeno" else False)]

    # list the filtered tasks
    list_tasks(tasks, clear_console=True)


def list_tasks(tasks: List[Task], clear_console: bool = False) -> None:
    console = ConsoleManager.get_instance()

    if clear_console:
        console.clear()

    table = Table(width=105)

    headers = ["ID", "Úkol", "Priorita", "Termín", "Stav"]
    task_rows = [(str(task.Id), task.Name, task.Priority.value, str(task.Deadline), "Dokončeno" if task.Status else "Nedokončeno") for task in tasks]

    for header in headers:
        table.add_column(header)

    for row in task_rows:
        table.add_row(*row)

    console = ConsoleManager.get_instance()
    console.print(table)
