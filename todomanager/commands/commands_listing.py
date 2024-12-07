from typing import List
from rich.table import Table
from todomanager.console.console import ConsoleManager, print_divider
from todomanager.entities.task import Task, TaskPriority

FILTERS = ["priority", "status"]


def list_tasks_with_filtering(tasks: List[Task]) -> None:
    console = ConsoleManager.get_instance()

    # get the desired filter
    while True:
        try:
            print_divider(text="Filtrování")
            console.print(f"Filtry: {', '.join(f"'{filter}'" for filter in FILTERS)}\n", style="bold")

            selected_filter = console.input("Zadejte filtr: ")

            if not selected_filter in FILTERS:
                raise ValueError("Neznámý filter, prosím zkuste to znovu.")

            break
        except ValueError as e:
            console.print(e, style="italic red")

    # filter by priority
    if selected_filter == "priority":
        while True:
            try:
                print_divider(text="Filtrování - Priority")
                console.print(f"Priority: {', '.join(f"'{priority.value}'" for priority in TaskPriority)}\n")

                # make sure that the priority is of valid value
                selected_priority = console.input("Zadejte prioritu pro filtrování: ")
                priority_parse_success, selected_priority = TaskPriority.try_parse(selected_priority)

                if not priority_parse_success or selected_priority == None:
                    raise ValueError("Neznámá priorita, prosím zkuste to znovu.")

                break
            except ValueError as e:
                console.print(e, style="italic red")

        tasks = list(filter(lambda task: task.Priority == selected_priority, tasks))
    # filter by status
    elif selected_filter == "status":
        while True:
            try:
                print_divider(text="Filtrování - Status")
                console.print(f"Statusy: {", ".join(f"'{status}'" for status in ["Dokončeno", "Nedokončeno"])}\n")

                selected_status = console.input("Zadejte status pro filtrování: ")

                # make sure that the status is of valid value
                if selected_status == "Dokončeno":
                    selected_status = True
                elif selected_status == "Nedokončeno":
                    selected_status = False
                else:
                    raise ValueError("Neznámá priorita, prosím zkuste to znovu.")

                break
            except ValueError as e:
                console.print(e, style="italic red")

        tasks = list(filter(lambda task: task.Status == selected_status, tasks))

    # finally list the filtered tasks
    list_tasks(tasks)


def list_tasks(tasks: List[Task]) -> None:
    table = Table(min_width=105)

    columns = ["ID", "Úkol", "Priorita", "Termín", "Stav"]
    rows = [(str(task.Id), task.Name, task.Priority.value, str(task.Deadline), "Dokončeno" if task.Status else "Nedokončeno") for task in tasks]

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row)

    console = ConsoleManager.get_instance()
    console.print(table)
