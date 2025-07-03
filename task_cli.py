import datetime as dt
import sys
import os
import json


class TaskTracker:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Error: tasks.json is corrupted. Starting with empty task list.")
        return []

    def save_tasks(self):
        with open(self.file_path, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        if not task:
            print("Task cannot be empty.")
            return
        # Check if the task already exists
        all_tasks = [t['description'] for t in self.tasks]
        if task in all_tasks:
            print(f"Task '{task}' already exists.")
            return
        
        # Generate unique ID by finding the max existing ID
        if self.tasks:
            new_id = max(t['id'] for t in self.tasks) + 1
        else:
            new_id = 1

        new_task = {
            "id": new_id,
            "description": task,
            "status": "todo",
            "createdAt": dt.datetime.now().isoformat(),
            "updatedAt": dt.datetime.now().isoformat()
        }

        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{task}' added successfully (ID: {new_id})")


    def list_tasks(self, command="all"):
        command = command.lower()
        valid_statuses = ["todo", "done", "in-progress"]

        if command == "all":
            filtered_tasks = self.tasks
        elif command in valid_statuses:
            filtered_tasks = [t for t in self.tasks if t["status"] == command]
        else:
            print(f"Unknown command: '{command}'")
            return

        if not filtered_tasks:
            print("No tasks found.")
            return

        print(f"Tasks ({command}):")
        for task in filtered_tasks:
            print(f"ID: {task['id']} | {task['description']} | Status: {task['status']} | Updated: {task['updatedAt']}")

    def update_task(self, task_id, new_description):
        for task in self.tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                task["updatedAt"] = dt.datetime.now().isoformat()
                self.save_tasks()
                print(f"Task ID {task_id} updated.")
                return
        print(f"No task found with ID {task_id}.")

    def mark_done(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                task["updatedAt"] = dt.datetime.now().isoformat()
                self.save_tasks()
                print(f"Task ID {task_id} marked as done.")
                return
        print(f"No task found with ID {task_id}.")

    def mark_in_progress(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "in-progress"
                task["updatedAt"] = dt.datetime.now().isoformat()
                self.save_tasks()
                print(f"Task ID {task_id} marked as in progress.")
                return
        print(f"No task found with ID {task_id}.")


    def remove_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed = self.tasks.pop(i)
                self.save_tasks()
                print(f"Task '{removed['description']}' (ID: {task_id}) removed.")
                return
        print(f"No task found with ID {task_id}.")


def main():
    tracker = TaskTracker()
    if len(sys.argv) < 2:
        print("Usage: task_cli.py <command> [<args>]")
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: task_cli.py add <task_description>")
            return
        task_description = " ".join(sys.argv[2:])
        tracker.add_task(task_description)

    elif command == "list":
        if len(sys.argv) > 2:
            tracker.list_tasks(sys.argv[2])
        else:
            tracker.list_tasks()

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: task_cli.py update <task_id> <new_description>")
            return
        task_id = int(sys.argv[2])
        new_description = " ".join(sys.argv[3:])
        tracker.update_task(task_id, new_description)

    elif command == "mark-done":
        if len(sys.argv) != 3:
            print("Usage: task_cli.py done <task_id>")
            return
        task_id = int(sys.argv[2])
        tracker.mark_done(task_id)

    elif command == "mark-in-progress":
        if len(sys.argv) != 3:
            print("Usage: task_cli.py in-progress <task_id>")
            return
        task_id = int(sys.argv[2])
        tracker.mark_in_progress(task_id)

    elif command == "delete":
        if len(sys.argv) != 3:
            print("Usage: task_cli.py remove <task_id>")
            return
        task_id = int(sys.argv[2])
        tracker.remove_task(task_id)

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
