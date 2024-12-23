
# Task Tracker CLI App

This project is a simple command-line application for managing a to-do list. It allows you to add, update, delete, and view tasks, with support for marking tasks as "todo", "in-progress", or "done". The data is stored in a JSON file, which keeps track of tasks and their respective status.

Project URL : https://roadmap.sh/projects/task-tracker


## Features
* Add a task: Add a new task with a description.

* Update a task: Modify the description of an existing task.

* Delete a task: Remove a task by its number or ID.

* Mark a task's status: Set the status of a task to "todo", "in_progress", or "done".

* List tasks: View all tasks or filter tasks by status (done, pending, in-progress).

* Help: View available commands and usage.



## Prerequisites
* Python 3

* No external dependencies are required for this script.


## Usage/Examples
You can interact with this script using different commands. Below are the available commands and their usage.
### Commands
* add: Add a new task to the to-do list.
```bash
python task.py add --task "Task description"
```
* update: Update the description of an existing task by specifying the task number and the new description.
```bash
python task.py update --number TASK_NUMBER --task "New description"
```
* delete: Delete a task by specifying the task number.
```bash
python task.py delete --number TASK_NUMBER
```
* delete_by_id: Delete a task by its unique ID.
```bash
python task.py delete_by_id --id TASK_ID
```
* mark: Mark a task as "todo", "in_progress", or "done" by specifying the task number and the desired status.
```bash
python task.py mark --number TASK_NUMBER --status STATUS
```
* list_done: List all tasks with the status "done".
```bash
python task.py list_done
```


* list_pending: List all tasks that are not marked as "done".

```bash
python task.py list_pending
```
* list_in_progress: List all tasks with the status "in_progress".

```bash
python task.py list_in_progress
```
* help: Display help message and list all available commands.

```bash
python task.py help
```



## How It Works

* The script reads from and writes to a task.json file.
* Each task is stored as a dictionary with the following fields:
  * id: A unique identifier for the task (UUID).
  * description: The description of the task.
  * status: The current status of the task (e.g., "todo", "in_progress", "done").
  * createdAt: Timestamp when the task was created.
  * updatedAt: Timestamp when the task was last updated.

## Example
```bash
python task.py add --task "Complete homework"
python task.py list
python task.py mark --number 1 --status "in_progress"
python task.py list_in_progress
python task.py update --number 1 --task "Complete homework and submit"
python task.py delete --number 1
```


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sahil-chukka)

[![gmail](https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sahil.chukka@gmail.com)


