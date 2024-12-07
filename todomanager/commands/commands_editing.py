from datetime import datetime
from typing import List
from todomanager.console.console import ConsoleManager, print_divider
from todomanager.entities.task import Task, TaskPriority


def add_task_command(tasks: List[Task]) -> List[Task]:
    console = ConsoleManager.get_instance()

    # get a value for the new task name
    while True:
        print_divider(text="Nový úkol - Jméno")
        task_name = console.input("Zadejte název úkolu: ").strip()

        if not task_name:
            console.print("Neplatný vstup, prosím zkuste to znovu.", style="italic red")
            continue
        break

    # get a value for the new task priority
    while True:
        print_divider(text="Nový úkol - Priorita")
        console.print(f"Priority: {', '.join(f"'{priority.value}'" for priority in TaskPriority)}\n")

        # make sure that the priority is of valid value
        task_priority = console.input("Zadejte prioritu: ").strip()
        priority_parse_success, task_priority = TaskPriority.try_parse(task_priority)

        if not priority_parse_success or task_priority == None:
            console.print("Neznámá priorita, prosím zkuste to znovu.", style="italic red")
            continue
        break

    # get a value for the new task deadline
    while True:
        try:
            print_divider(text="Nový úkol - Termín splnění")

            # make sure that the priority is of valid value
            task_deadline = console.input("Zadejte termín splnění (YYYY-MM-DD): ").strip()

            if task_deadline:
                task_deadline = datetime.strptime(task_deadline, "%Y-%m-%d")
            break
        except ValueError as e:
            console.print("Neplatné datum, prosím zkuste to znovu.", style="italic red")

    tasks.append(
        Task(
            Id=max(task.Id for task in tasks) + 1,
            Name=task_name,
            Priority=task_priority,
            Deadline=task_deadline,
            Status=False,
        )
    )

    console.print(f"Úkol '{task_name}' byl přidán.")

    return tasks


def remove_task_command(tasks: List[Task]) -> List[Task]:
    console = ConsoleManager.get_instance()

    # get the id of the task to remove
    while True:
        try:
            task_to_remove_id = int(console.input("Zadejte ID úkolu, který chcete odstranit: "))
        except ValueError as e:
            console.print("Neplatný vstup, prosím zkuste to znovu.", style="italic red")
            continue

        if task_to_remove_id <= 0:
            console.print("Neplatný vstup, prosím zkuste to znovu.", style="italic red")
            continue

        if task_to_remove_id not in list(task.Id for task in tasks):
            console.print("Úkol s tímto ID neexistuje, prosím zkuste to znovu.", style="italic red")
            continue
        break

    task_to_remove = [task for task in tasks if task.Id == task_to_remove_id][0]
    tasks.remove(task_to_remove)

    console.print(f"Úkol '{task_to_remove.Name}' byl odstraněn.")

    return tasks


def complete_task_command(tasks: List[Task]) -> List[Task]:
    console = ConsoleManager.get_instance()

    # get the id of the task to complete
    while True:
        try:
            task_to_complete_id = int(console.input("Zadejte ID úkolu, který chcete splnit: "))
        except ValueError as e:
            console.print("Neplatný vstup, prosím zkuste to znovu.", style="italic red")
            continue

        if task_to_complete_id <= 0:
            console.print("Neplatný vstup, prosím zkuste to znovu.", style="italic red")
            continue

        if task_to_complete_id not in list(task.Id for task in tasks):
            console.print("Úkol s tímto ID neexistuje, prosím zkuste to znovu.", style="italic red")
            continue
        break

    task_to_complete = [task for task in tasks if task.Id == task_to_complete_id][0]
    task_to_complete.Status = True

    console.print(f"Úkol '{task_to_complete.Name}' byl označen jako dokončený.")

    return tasks


def edit_task_command(tasks: List[Task]) -> List[Task]:
    console = ConsoleManager.get_instance()

    # get the id of the task to edit
    while True:
        try:
            task_to_edit_id = int(console.input("Zadejte ID úkolu, který chcete upravit: "))
        except ValueError as e:
            console.print("Neplatný vstup, prosím zkuste to znovu.", style="italic red")
            continue

        if task_to_edit_id <= 0:
            console.print("Neplatný vstup, prosím zkuste to znovu.", style="italic red")
            continue

        if task_to_edit_id not in list(task.Id for task in tasks):
            console.print("Úkol s tímto ID neexistuje, prosím zkuste to znovu.", style="italic red")
            continue
        break

    task_to_edit = [task for task in tasks if task.Id == task_to_edit_id][0]

    # get a value for the new edited task name
    while True:
        print_divider(text="Editace úkolu - Jméno")
        new_task_name = console.input(f"Zadejte nový název úkolu (aktuálně '{task_to_edit.Name}'): ").strip()

        if not new_task_name:
            console.print("Neplatný vstup, prosím zkuste to znovu.", style="italic red")
            continue
        break

    # get a value for the new edited task priority
    while True:
        print_divider(text="Editace úkolu - Priorita")
        console.print(f"Priority: {', '.join(f"'{priority.value}'" for priority in TaskPriority)}\n")

        # make sure that the priority is of valid value
        new_task_priority = console.input(f"Zadejte novou prioritu (aktuálně '{task_to_edit.Priority.value}'): ").strip()
        priority_parse_success, new_task_priority = TaskPriority.try_parse(new_task_priority)

        if not priority_parse_success or new_task_priority == None:
            console.print("Neznámá priorita, prosím zkuste to znovu.", style="italic red")
            continue
        break

    # get a value for the new edited task deadline
    while True:
        try:
            print_divider(text="Editace úkolu - Termín splnění")

            new_task_deadline = console.input(
                f"Zadejte termín splnění (YYYY-MM-DD)(aktuálně '{task_to_edit.Deadline}'): "
            ).strip()

            if new_task_deadline:
                new_task_deadline = datetime.strptime(new_task_deadline, "%Y-%m-%d")
            else:
                new_task_deadline = None

            break
        except ValueError as e:
            console.print("Neplatné datum, prosím zkuste to znovu.", style="italic red")

    task_to_edit.Name = new_task_name
    task_to_edit.Priority = new_task_priority
    task_to_edit.Deadline = new_task_deadline

    console.print(f"Úkol '{task_to_edit.Name}' byl upraven.")

    return tasks
