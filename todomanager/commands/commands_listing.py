from typing import List
from rich.table import Table
from todomanager.console.console import ConsoleManager, print_divider
from todomanager.entities.task import Task, TaskPriority

FILTERS = ["priority", "status"]


def list_tasks_command(tasks: List[Task]) -> None:
    console = ConsoleManager.get_instance()

    # prompt for the desired filter
    while True:
        print_divider(text="Filtrování")

        available_filters = ", ".join(f"'{filter}'" for filter in FILTERS)
        console.print(f"Filtry: {available_filters}\n", style="bold")

        selected_filter = console.input("Zadejte filtr: ").strip()

        if selected_filter not in FILTERS:
            console.print("Neznámý filtr, prosím zkuste to znovu.", style="italic red")
        else:
            break

    # filter by priority
    if selected_filter == "priority":
        while True:
            print_divider(text="Filtrování - Priority")

            available_priorities = ", ".join(f"'{priority.value}'" for priority in TaskPriority)
            console.print(f"Priority: {available_priorities}\n")

            entered_priority = console.input("Zadejte prioritu pro filtrování: ").strip()
            is_valid_priority, parsed_priority = TaskPriority.try_parse(entered_priority)

            if not is_valid_priority or parsed_priority is None:
                console.print("Neznámá priorita, prosím zkuste to znovu.", style="italic red")
            else:
                break

        tasks = [task for task in tasks if task.Priority == parsed_priority]

    # filter by status
    elif selected_filter == "status":
        while True:
            print_divider(text="Filtrování - Status")
            console.print(f"Statusy: {", ".join(f"'{status}'" for status in ["Dokončeno", "Nedokončeno"])}\n")

            entered_status = console.input("Zadejte status pro filtrování: ").strip()

            if entered_status == "Dokončeno":
                status_filter = True
            elif entered_status == "Nedokončeno":
                status_filter = False
            else:
                console.print("Neznámý status, prosím zkuste to znovu.", style="italic red")
                continue

            break

        tasks = [task for task in tasks if task.Status == status_filter]

    # list the filtered tasks
    list_tasks(tasks)


def list_tasks(tasks: List[Task]) -> None:
    table = Table(min_width=105)

    headers = ["ID", "Úkol", "Priorita", "Termín", "Stav"]
    task_rows = [
        (str(task.Id), task.Name, task.Priority.value, str(task.Deadline), "Dokončeno" if task.Status else "Nedokončeno")
        for task in tasks
    ]

    for header in headers:
        table.add_column(header)

    for row in task_rows:
        table.add_row(*row)

    console = ConsoleManager.get_instance()
    console.print(table)
