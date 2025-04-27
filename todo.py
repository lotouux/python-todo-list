# To-do list
import json  # Store lists and dictionaries

filename = "tasks.json"  # File where the tasks will be saved

def load_tasks():
    try:
        # Try to open the file in read mode, load the data from the JSON file to the list, and ensure special characters are read correctly
        with open(filename, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        return tasks
    except FileNotFoundError:
        # If the file is not found, return an empty list
        print(f"'{filename}' not found. Starting with an empty list.") 
        return []
    except json.JSONDecodeError:
        # If the file has invalid JSON format, return an empty list
        print(f"Error decoding JSON from '{filename}'. Starting with an empty list.")
        return []
    except Exception as e:
        # Catch other possible reading errors
        print(f"An unexpected error occurred while loading tasks: {e}")
        return []

def save_tasks():
    global tasks  # Use the global tasks variable
    try:
        # Open the file in write mode to overwrite previous content
        with open(filename, 'w', encoding='utf-8') as f:
            # Save the 'tasks' list (global) to the file 'f' in JSON format
            # ensure_ascii=False allows special characters like 'ç' or accents
            # indent=4 formats the JSON file in a readable way (with indentation)
            json.dump(tasks, f, ensure_ascii=False, indent=4)
    except Exception as e:
        # Catch possible writing errors
        print(f"An unexpected error occurred while saving tasks: {e}")

# Menu
def show_menu():
    print("TO-DO LIST")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. Edit task")
    print("6. Exit")

def add_task():
    task = input("Enter the new task: ")
    tasks.append({"title": task, "completed": False})
    print("Task added!")

def list_tasks():
    print("Tasks")
    if not tasks:
        print("No tasks found.")
        return
    
    for i, task in enumerate(tasks):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i + 1}. {task['title']} [{status}]")

def mark_completed():
    list_tasks()
    try:
        i = int(input("Enter the number of the task to mark as completed: ")) - 1
        tasks[i]["completed"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid input.")

def remove_task():
    list_tasks()
    try:
        i = int(input("Enter the number of the task to remove: ")) - 1
        tasks.pop(i)
        print("Task removed!")
    except (IndexError, ValueError):
        print("Invalid input.")

def edit_task():
    list_tasks()
    try:
        i = int(input("Enter the number of the task to edit: ")) - 1
        new_title = input("Enter the new task title: ")
        tasks[i]["title"] = new_title
        print("Task edited!")
    except (IndexError, ValueError):
        print("Invalid input.")

# Main initialization
# Load the tasks from the file when starting the program
tasks = load_tasks()

# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        edit_task()
    elif choice == "6":
        print("Saving tasks...")
        save_tasks()
        print("Exiting... See you later!")
        break
    else:
        print("Invalid option.")
