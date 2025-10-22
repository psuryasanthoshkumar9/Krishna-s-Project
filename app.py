# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_no - 1)
        print(f"Task '{removed}' removed!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Main program
# To-Do List App - Version 2
# Added features: Save/Load from file, Mark as Done, Separate Pending/Completed tasks

import os

FILE_NAME = "tasks.txt"

# Each task = {"task": "Buy milk", "done": False}
tasks = []


def load_tasks():
    """Load tasks from file if it exists."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, status = line.strip().split("|")
                tasks.append({"task": name, "done": status == "True"})


def save_tasks():
    """Save all tasks to file."""
    with open(FILE_NAME, "w") as f:
        for t in tasks:
            f.write(f"{t['task']}|{t['done']}\n")


def show_menu():
    print("\n--- To-Do List App v2 ---")
    print("1. View All Tasks")
    print("2. View Pending Tasks")
    print("3. View Completed Tasks")
    print("4. Add New Task")
    print("5. Mark Task as Done")
    print("6. Remove Task")
    print("7. Exit")


def view_tasks(filter_by=None):
    if not tasks:
        print("No tasks found!")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        if filter_by == "pending" and t["done"]:
            continue
        if filter_by == "done" and not t["done"]:
            continue
        status = "✅ Done" if t["done"] else "⏳ Pending"
        print(f"{i}. {t['task']} — {status}")


def add_task():
    name = input("Enter a new task: ")
    tasks.append({"task": name, "done": False})
    save_tasks()
    print(f"Task '{name}' added!")


def mark_done():
    view_tasks("pending")
    try:
        task_no = int(input("Enter task number to mark as done: "))
        tasks[task_no - 1]["done"] = True
        save_tasks()
        print("Task marked as done ✅")
    except (IndexError, ValueError):
        print("Invalid number!")


def remove_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_no - 1)
        save_tasks()
        print(f"Removed: {removed['task']}")
    except (IndexError, ValueError):
        print("Invalid number!")


# --- Main Program ---
load_tasks()

while True:
    show_menu()
    choice = input("Enter your choice (1–7): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        view_tasks("pending")
    elif choice == '3':
        view_tasks("done")
    elif choice == '4':
        add_task()
    elif choice == '5':
        mark_done()
    elif choice == '6':
        remove_task()
    elif choice == '7':
        print("Saving and exiting... 👋")
        save_tasks()
        break
    else:
        print("Invalid choice! Please try again.")


