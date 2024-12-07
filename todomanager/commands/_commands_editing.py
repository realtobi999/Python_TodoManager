from datetime import datetime
from typing import List
from todomanager.console.console import ConsoleManager
from todomanager.entities.task import Task, TaskPriority


def add_task_command(tasks: List[Task]) -> List[Task]:
    console = ConsoleManager.get_instance()

    # get a value for the new task name
    ConsoleManager.print_divider(text="Nový úkol - Jméno")
    task_name = ConsoleManager.input_string(text="Zadejte název úkolu: ", conditions=[lambda name: name.strip()]).strip()

    # get a value for the new task priority
    ConsoleManager.print_divider(text="Nový úkol - Priorita")
    available_priorities = [priority.value for priority in TaskPriority]
    console.print(f"Priority: {", ".join(f"'{priority}'" for priority in available_priorities)}\n")

    task_priority = TaskPriority(
        ConsoleManager.input_string(
            text="Zadejte prioritu: ",
            error_message="Neznámá hodnota pro prioritu, zkuste to znovu.",
            conditions=[lambda priority: priority.strip() in available_priorities],
        )
    )

    # get a value for the new task deadline
    ConsoleManager.print_divider(text="Nový úkol - Termín splnění")
    task_deadline = ConsoleManager.input_string(
        text="Zadejte termín splnění (YYYY-MM-DD): ",
        conditions=[lambda date: datetime.strptime(date, "%Y-%m-%d") if date else True],
    )

    new_task = Task(
        Id=max(task.Id for task in tasks) + 1,
        Name=task_name,
        Priority=task_priority,
        Deadline=task_deadline if task_deadline else None,
        Status=False,
    )
    tasks.append(new_task)

    console.print(f"\nÚkol byl přidán.", style="bold green")

    return tasks


def remove_task_command(tasks: List[Task]) -> List[Task]:
    console = ConsoleManager.get_instance()
    ConsoleManager.print_divider(text="Odstranění úkolu")

    # get the id of the task to remove
    task_to_remove_id = ConsoleManager.input_int(
        text="Zadejte ID úkolu, který chcete odstranit: ",
        error_message="Úkol s tímto ID nebyl nalezen, zkuste to prosím znovu.",
        conditions=[lambda n: n > 0, lambda n: n in list(task.Id for task in tasks)],
    )

    task_to_remove = [task for task in tasks if task.Id == task_to_remove_id][0]
    tasks.remove(task_to_remove)

    console.print(f"Úkol '{task_to_remove.Name}' byl odstraněn.", style="bold green")

    return tasks


def complete_task_command(tasks: List[Task]) -> List[Task]:
    console = ConsoleManager.get_instance()

    # get the id of the task to complete
    task_to_complete_id = ConsoleManager.input_int(
        text="Zadejte ID úkolu, který chcete dokončit: ",
        error_message="Úkol s tímto ID nebyl nalezen, zkuste to prosím znovu.",
        conditions=[lambda n: n > 0, lambda n: n in list(task.Id for task in tasks)],
    )

    task_to_complete = [task for task in tasks if task.Id == task_to_complete_id][0]

    # if the task is  already  completed
    # cancel the completion process
    if task_to_complete.Status:
        console.print(f"\nÚkol je již označen jako dokončený.", style="bold green")
        return tasks

    task_to_complete.Status = True

    console.print(f"\nÚkol byl označen jako dokončený.", style="bold green")

    return tasks


def edit_task_command(tasks: List[Task]) -> List[Task]:
    console = ConsoleManager.get_instance()
    ConsoleManager.print_divider(text="Editace úkolu")

    # get the id of the task to edit
    task_to_edit_id = ConsoleManager.input_int(
        text="Zadejte ID úkolu, který chcete upravit: ",
        error_message="Úkol s tímto ID nebyl nalezen, zkuste to prosím znovu.",
        conditions=[lambda n: n > 0, lambda n: n in list(task.Id for task in tasks)],
    )

    task_to_edit = [task for task in tasks if task.Id == task_to_edit_id][0]

    # get a value for the new edited task name
    ConsoleManager.print_divider(text="Editace úkolu - Jméno")
    new_task_name = ConsoleManager.input_string(text=f"Zadejte nový název úkolu (aktuálně '{task_to_edit.Name}'): ").strip()

    # get a value for the new edited task priority
    ConsoleManager.print_divider(text="Editace úkolu - Priorita")
    available_priorities = [priority.value for priority in TaskPriority]
    console.print(f"Priority: {", ".join(f"'{priority}'" for priority in available_priorities)}\n")

    new_task_priority = ConsoleManager.input_string(
        text="Zadejte prioritu: ",
        error_message="Neznámá hodnota pro prioritu, zkuste to znovu.",
        conditions=[lambda priority: True if priority.strip() == "" else priority.strip() in available_priorities],
    )

    # get a value for the new edited task deadline
    ConsoleManager.print_divider(text="Editace úkolu - Termín splnění")
    new_task_deadline = ConsoleManager.input_string(
        text=f"Zadejte termín splnění (YYYY-MM-DD)(aktuálně '{task_to_edit.Deadline}'): ",
        conditions=[lambda date: datetime.strptime(date, "%Y-%m-%d") if date else True],
    )

    # check if the new value is empty if
    # so then assign it otherwise  leave
    # the old value as it is
    task_to_edit.Name = new_task_name if new_task_name else task_to_edit.Name
    task_to_edit.Priority = TaskPriority(new_task_priority) if new_task_priority else task_to_edit.Priority
    task_to_edit.Deadline = new_task_deadline if new_task_deadline else task_to_edit.Deadline

    console.print(f"Úkol byl upraven.", style="bold green")

    return tasks
