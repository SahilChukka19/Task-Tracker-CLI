#import libraries
import os
import json
import argparse
import uuid
from datetime import datetime


TASK_FILE = "task.json"

# Load tasks from the JSON file
def load():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the JSON file
def save_task(tasks):
    with open(TASK_FILE,"w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_tasks(description):
    tasks = load()
    task = {
        "id" : str(uuid.uuid4()),
        "description" : description,
        "status" : "todo",
        "createdAt" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_task(tasks)
    print(f"Task added successfully : {description}")

# Update Existing Task
def update_task(task_number, new_description):
    tasks = load()
    if 0 < task_number <= len(tasks):
        tasks[task_number -1]["description"] = new_description
        tasks[task_number - 1]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_task(tasks)
        print(f"Task {task_number} updated to: {new_description}")
    else:
        print("Invalid task number")

# Delete task by number
def delete_task(task_number):
    tasks = load()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_task(tasks)
        print(f"Task deleted: [ID: {removed_task['id']}] {removed_task['description']}")
    else:
        print("Invalid task number.")

# Check Status of the task
def status_mark(task_number, status):
    tasks = load()
    if 0 < task_number <= len(tasks):
        if status in ["todo","in_progress","done"]:
            tasks[tasks - 1]["status"] = status
            tasks[tasks - 1]["updatedAT"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_task(tasks)
            print(f"Task {task_number} marked as {status.replace('_', ' ')}.")
        else:
            print("Invalid status. Use 'todo', 'in_progress', or 'done'.")

    else:
        print("Invalid task number.")

# List all tasks
def list_tasks():
    tasks = load()
    if not tasks:
        print("Task not found")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. [ID: {task['id']}]")
        print(f"   Description: {task['description']}")
        print(f"   Status: {task['status']}")
        print(f"   Created At: {task['createdAt']}")
        print(f"   Updated At: {task['updatedAt']}\n")

# List Completed Tasks
def list_done_tasks():
    tasks = load()
    done_tasks = [task for task in tasks if task["status"] == "done"]
    if done_tasks:
        for i, task in enumerate(done_tasks, 1):
            print(f"{i}. [ID: {task['id']}] {task['description']}")
            print(f"   Status: {task['status']}")
            print(f"   Created At: {task['createdAt']}")
            print(f"   Updated At: {task['updatedAt']}\n")
    else:
        print("No done tasks found.")

#List pending tasks
def list_pending_tasks():
    tasks = load()
    pending_tasks = [task for task in tasks if task["status"] != "done"]
    if pending_tasks:
        for i, task in enumerate(pending_tasks, 1):
            print(f"{i}. [ID: {task['id']}] {task['description']}")
            print(f"   Status: {task['status']}")
            print(f"   Created At: {task['createdAt']}")
            print(f"   Updated At: {task['updatedAt']}\n")
    else:
        print("No pending tasks found.")

# List in progress tasks
def list_in_progress_tasks():
    tasks = load()
    in_progress_tasks = [task for task in tasks if task["status"] == "in_progress"]
    if in_progress_tasks:
        for i, task in enumerate(in_progress_tasks, 1):
            print(f"{i}. [ID: {task['id']}] {task['description']}")
            print(f"   Status: {task['status']}")
            print(f"   Created At: {task['createdAt']}")
            print(f"   Updated At: {task['updatedAt']}\n")
    else:
        print("No in-progress tasks found.")

# To display all available commands
def display_help():
    print("\nTo-Do List CLI App Commands:")
    print("  add --task \"TASK_DESCRIPTION\"       : Add a new task to the to-do list")
    print("  update --number TASK_NUMBER --task \"NEW_DESCRIPTION\"")
    print("                                       : Update an existing task's description")
    print("  delete --number TASK_NUMBER          : Delete a task by its number")
    print("  mark --number TASK_NUMBER --status STATUS")
    print("                                       : Mark a task as 'todo', 'in_progress', or 'done'")
    print("  list                                 : List all tasks")
    print("  list_done                            : List all tasks with status 'done'")
    print("  list_pending                         : List all tasks with status 'pending'")
    print("  list_in_progress                     : List all tasks with status 'in_progress'")
    print("  help                                 : Show this help message\n")


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Manage your to-do list")

    # Define the subcommands
    subparsers = parser.add_subparsers(dest="command")

    # Add subcommands for each task action
    subparsers.add_parser("help", help="Show help message")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("--task", required=True, help="Description of the task")

    update_parser = subparsers.add_parser("update", help="Update a task's description")
    update_parser.add_argument("--number", type=int, required=True, help="Task number")
    update_parser.add_argument("--task", required=True, help="New description for the task")

    delete_parser = subparsers.add_parser("delete", help="Delete a task by its number")
    delete_parser.add_argument("--number", type=int, required=True, help="Task number")

    mark_parser = subparsers.add_parser("mark", help="Mark a task as done, in_progress, or todo")
    mark_parser.add_argument("--number", type=int, required=True, help="Task number")
    mark_parser.add_argument("--status", required=True, choices=["todo", "in_progress", "done"], help="New status for the task")

    subparsers.add_parser("list", help="List all tasks")
    subparsers.add_parser("list_done", help="List all done tasks")
    subparsers.add_parser("list_pending", help="List all pending tasks")
    subparsers.add_parser("list_in_progress", help="List all in-progress tasks")

    # Parse the arguments
    args = parser.parse_args()

    # Call corresponding function based on the command
    if args.command == "help":
        display_help()
    elif args.command == "add":
        add_tasks(args.task)
    elif args.command == "update":
        update_task(args.number, args.task)
    elif args.command == "delete":
        delete_task(args.number)
    elif args.command == "mark":
        status_mark(args.number, args.status)
    elif args.command == "list":
        list_tasks()
    elif args.command == "list_done":
        list_done_tasks()
    elif args.command == "list_pending":
        list_pending_tasks()
    elif args.command == "list_in_progress":
        list_in_progress_tasks()


if __name__ == "__main__":
    main()






