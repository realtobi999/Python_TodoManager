import os
import todomanager

TASKS_FILE_PATH = "./data/todo_tasks.txt"

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")

    status = todomanager.run(TASKS_FILE_PATH)

    # if everything went well exit with status code 0
    if status == 0:
        exit(0)
