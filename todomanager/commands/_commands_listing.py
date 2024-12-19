from datetime import datetime
from typing import List
from rich.table import Table
from todomanager.console.console import ConsoleManager
from todomanager.entities.enums import Filter
from todomanager.entities.task import Task, TaskPriority


def list_tasks_with_filtering(tasks: List[Task]) -> None:
    console = ConsoleManager.get_instance()

    # Prompt the user for the desired filter.
    ConsoleManager.print_divider(text="Zobrazení úkolů - Filtrování")
    console.print(f"Hodnota pro filtrování: {", ".join(f"'{filter.value}'" for filter in Filter)}\n")

    selected_filter = Filter(
        ConsoleManager.input_string(
            text="Zadejte filtr: ",
            error_message="Neznámá hodnota pro filtrování, zkuste to znovu.",
            conditions=[lambda filter: Filter.try_parse(filter.strip())],
        ).strip()
    )

    # Filter by priority.
    if selected_filter == Filter.PRIORITY:
        ConsoleManager.print_divider(text="Zobrazení úkolů - Filtrování - Dle priority")
        console.print(f"Priority: {", ".join(f"'{priority.value}'" for priority in TaskPriority)}\n")

        task_priority = TaskPriority(
            ConsoleManager.input_string(
                text="Zadejte prioritu: ",
                error_message="Neznámá hodnota pro prioritu, zkuste to znovu.",
                conditions=[lambda priority: TaskPriority.try_parse(priority.strip())[0]],
            ).strip()
        )
        filtered_tasks = [task for task in tasks if task.priority == task_priority]

    # Filter by status.
    elif selected_filter == Filter.STATUS:
        ConsoleManager.print_divider(text="Zobrazení úkolů - Filtrování - Dle stavu")
        available_statuses = ["Dokončeno", "Nedokončeno"]
        console.print(f"Statusy: {", ".join(f"'{status}'" for status in available_statuses)}\n")

        task_status = ConsoleManager.input_string(text="Zadejte stav: ", conditions=[lambda status: status.strip() in available_statuses]).strip()
        filtered_tasks = [task for task in tasks if task.status == (True if task_status == "Dokončeno" else False)]

    # Filter by deadline.
    elif selected_filter == Filter.DEADLINE:
        ConsoleManager.print_divider(text="Zobrazení úkolů - Filtrování - Dle deadline")

        deadline_limit = datetime.strptime(
            ConsoleManager.input_string(text="Zadejte datum pro filtrování (YYYY-MM-DD): ", conditions=[lambda date_str: datetime.strptime(date_str, "%Y-%m-%d")]), "%Y-%m-%d"
        )

        filtered_tasks = [task for task in tasks if task.deadline and task.deadline <= deadline_limit]

    # Finally list the filtered tasks.
    list_tasks(filtered_tasks, clear_console=True)


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
