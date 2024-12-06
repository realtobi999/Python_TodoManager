import os
import todomanager

TASKS_FILE_PATH = "./data/todo_tasks.txt"

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")

    todomanager.run(TASKS_FILE_PATH)
