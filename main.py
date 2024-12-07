import os
import traceback
import todomanager
from iridis import get_number_from_user, print_error

TASKS_FILE_PATH = "./data/todo_tasks.txt"

if __name__ == "__main__":
    while True:
        try:
            os.system("clear" if os.name == "posix" else "cls")

            status = todomanager.run(TASKS_FILE_PATH)

            # if everything went well exit with status code 0
            if status == 0:
                exit(0)
        except Exception as e:
            print_error(f"Chyba v systému: {e}")

            # ask for debug mode
            print("\nDEBUG MODE? (0/1)")
            should_debug = get_number_from_user(
                input_text="=> ",
                error_message="Neplatný vstup.",
                conditions=[lambda n: n == 0 or n == 1],
            )
            if should_debug == 1:
                traceback.print_exception(e.__cause__)

            # ask for restart of the application
            print("\nChcete zkusit aplikaci restartovat? (0/1)")
            should_continue = get_number_from_user(
                input_text="=> ",
                error_message="Neplatný vstup.",
                conditions=[lambda n: n == 0 or n == 1],
            )
            if should_continue == 1:
                continue
            if should_continue == 0:
                exit(0)
