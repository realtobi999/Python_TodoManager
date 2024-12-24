# Tasks Manager

## Table of Contents

- **[Summary](#summary)**
- **[How to run?](#how-to-run)**
- **[Extensions](#extensions)**
- **[Notes](#notes)**

## Summary

- **Add Task:** Users can add a new task with the following properties:
  - **Task Name (required):** A descriptive name for the task.
  - **Priority (optional):** Can be `low`, `medium` (default), or `high`.
  - **Deadline (optional):** A completion date in the format `YYYY-MM-DD`, or left empty.
  - **Status:** Automatically set to `incomplete` when a task is created.

- **View Tasks:** Users can view a list of all tasks, including their properties. Filtering options:
  - By **Priority** (e.g., only tasks with `high` priority).
  - By **Status** (`complete` or `incomplete`).
  - By **Deadline** (e.g., tasks with an approaching due date).

- **Remove Task:** Users can delete tasks by specifying their ID or name.

- **Mark Task as Complete:** Users can mark any task as `complete`. Completed tasks remain in the list for reference.

- **Edit Task:** Users can update the properties of an existing task, including name, priority, deadline, and status.

- **Save and Load Tasks:**
  - On exit, tasks are saved to a file in either CSV or JSON format.
  - On startup, the application loads tasks from the saved file and resumes from the previous state.

## How to run?

**Required Libraries:**

- `rich`
  - Install by running:

    ```bash
    pip install rich
    ```

Before running the app, ensure that a folder named `data` exists and contains a file `todo_task.txt`.  
This file is used to store tasks.  **DO NOT MODIFY THIS FILE MANUALLY**. Modifying it could lead to errors such as:

```bash
Chyba v systému: Chyba během načítání úkolů.

DEBUG MODE? (0/1)
=> 1
Traceback (most recent call last):
  ...
ValueError: Invalid format on line 1: Invalid priority 'Vysoká': Must be one of LOW (nízká), MID (střední), HIGH (vysoká).
```

Execute the program in vscode or using a simple command in the root folder:

``` bash
python3 main.py
```

## Extensions

- Add support for JSON
- Add support for notifications

## Notes

This project involved working with the **Rich** terminal library, where I gained experience in implementing parsing logic and handling user input validation.
One key takeaway from this project was the importance of making sure an application does not crash under any circumstances. It highlighted the need to always safely handle errors and ensure the application exits gracefully, with a clear prompt for the user.
