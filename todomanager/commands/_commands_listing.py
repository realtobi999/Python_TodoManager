from typing import List
from rich.table import Table
from todomanager.console.console import ConsoleManager
from todomanager.entities.enums import Filter
from todomanager.entities.task import Task, TaskPriority


def list_tasks_with_filtering(tasks: List[Task]) -> None:
    console = ConsoleManager.get_instance()

    # Prompt the user for the desired filter.
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

    # Filter by priority.
    if selected_filter == Filter.PRIORITY:
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

        tasks = [task for task in tasks if task.priority == task_priority]

    # Filter by status.
    elif selected_filter == Filter.STATUS:
        ConsoleManager.print_divider(text="Zobrazení úkolů - Filtrování - Dle stavu")
        available_statuses = ["Dokončeno", "Nedokončeno"]
        console.print(f"Statusy: {", ".join(f"'{status}'" for status in available_statuses)}\n")

        task_status = ConsoleManager.input_string("Zadejte stav: ", conditions=[lambda status: status.strip() in available_statuses]).strip()

        tasks = [task for task in tasks if task.status == (True if task_status == "Dokončeno" else False)]

    # Finally list the filtered tasks.
    list_tasks(tasks, clear_console=True)


def list_tasks(tasks: List[Task], clear_console: bool = False) -> None:
    if clear_console:
        ConsoleManager.clear_console()

    table = Table(width=105)

    headers = ["ID", "Úkol", "Priorita", "Termín", "Stav"]
    task_rows = [
        (
            str(task.id),
            task.name,
            task.priority.value,
            task.deadline.strftime("%Y-%m-%d") if task.deadline else "Bez termínu",
            "Dokončeno" if task.status else "Nedokončeno",
        )
        for task in tasks
    ]

    for header in headers:
        table.add_column(header)

    for row in task_rows:
        table.add_row(*row)

    console = ConsoleManager.get_instance()
    console.print(table)
