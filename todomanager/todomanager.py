import traceback
from pathlib import Path
from todomanager.commands.command_manager import CommandTaskService, get_command_from_user, run_command
from todomanager.console.console import ConsoleManager
from todomanager.entities.enums import Command
from todomanager.parsers.file_task_parser import parse_tasks
from todomanager.savers.file_task_saver import save_tasks


def run(tasks_file_path: str) -> int:
    """
    Runs the application and takes care of top level error handling.

    Args:
        tasks_file_path (str): Path to the file, where the tasks are stored.

    Returns:
        int: Returns 0 if the application executed  successfully,  or  1  if  an
        unexpected error occurred.
    """
    ConsoleManager.clear_console()
    console = ConsoleManager.get_instance()

    # Wrap the entire application in a  try-except
    # block to handle  errors  gracefully.  If  an
    # exception occurs, provide the user  with  an
    # option to view the full stack  trace  (DEBUG
    # MODE) and  decide  whether  to  restart  the
    # application.
    try:
        # Parse the tasks from the provided file.
        try:
            tasks = parse_tasks(file_path=Path(tasks_file_path))
        except Exception as e:
            raise Exception("Error occurred while loading tasks.") from e

        # Start the application and display the parsed tasks to the user.
        try:
            ConsoleManager.print_intro_ascii_logo()
            ConsoleManager.print_divider(text="Current Task List")
            CommandTaskService.list_tasks(tasks)
        except Exception as e:
            raise Exception("Error occurred during application startup.") from e

        # Continuously handle user input commands.
        while True:
            try:
                selected_command = get_command_from_user()

                # If the EXIT command is selected, save tasks  and
                # terminate the application with a status code  of
                # 0, indicating successful execution.
                if selected_command == Command.EXIT:
                    save_tasks(file_path=Path(tasks_file_path), tasks=tasks)
                    console.print("Tasks have been saved. Exiting the application.")
                    return 0
                else:
                    # Process the selected command.
                    run_command(selected_command, tasks, Path(tasks_file_path))

            except Exception as e:
                raise Exception("Error occurred while processing commands.") from e

    except Exception as e:
        ConsoleManager.print_error_ascii_logo()
        console.print(f"System error: {e}", style="bold red")

        # Prompt the user to enable DEBUG MODE to
        # view the full exception stack trace.
        console.print("\n[reset]DEBUG MODE? (0/1)")
        should_debug = ConsoleManager.input_int(
            text="=> ",
            error_message="Invalid input.",
            conditions=[lambda n: n == 0 or n == 1],
        )
        if should_debug == 1:
            traceback.print_exception(e.__cause__)

        # Ask the user if they want to restart the application.
        console.print("\n[reset]Do you want to restart the application? (0/1)")
        should_continue = ConsoleManager.input_int(
            text="=> ",
            error_message="Invalid input.",
            conditions=[lambda n: n == 0 or n == 1],
        )
        if should_continue == 1:
            return run(tasks_file_path)  # Restart the application.
        if should_continue == 0:
            return 1  # Exit the application with the status code inditacing error.
