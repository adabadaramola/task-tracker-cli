# 📝 Task Tracker CLI https://roadmap.sh/projects/task-tracker

A simple command-line tool to track and manage your tasks.  
Easily add, update, delete, and list your tasks — all from your terminal.

## 🚀 Features

- Add new tasks with descriptions
- Update existing task descriptions
- Delete tasks
- Mark tasks as:
  - ✅ Done
  - 🔄 In Progress
- List tasks by:
  - All
  - Status (done, todo, in-progress)
- Task data is stored persistently in a local `tasks.json` file

## 📦 Example Usage

```bash
# Add a new task
python task_cli.py add "Buy groceries"

# Update a task
python task_cli.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task_cli.py delete 1

# Mark task as in progress
python task_cli.py mark-in-progress 2

# Mark task as done
python task_cli.py mark-done 2

# List all tasks
python task_cli.py list

# List tasks by status
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress
