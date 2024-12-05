import os
import todomanager

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")

    todomanager.run()
