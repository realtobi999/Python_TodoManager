import os
import todomanager

TASKS_FILE_PATH = "./data/todo_tasks.txt"

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")

    status = todomanager.run(TASKS_FILE_PATH)

    # Exit with status code  0  if  execution  was
    # successful; otherwise, exit with status code
    # 1 to indicate an error.
    if status == 0:
        exit(0)
    elif status == 1:
        exit(1)
