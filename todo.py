# To-do list

tasks = []

# menu
def show_menu():
    print("TO-DO LIST")
    print("1. Add task")
    print("2.List Tasks")
    print("3.Mark tasks as completed")
    print("4.Remove task")
    print("5.Edit task")
    print("6.Exit")

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
        print("Task removed")
    except (IndexError, ValueError):
        print("Invalid input.")

def edit_task():
    list_tasks()
    try:
        i = int(input("Enter the number of the task to edit: ")) - 1
        new_title = (input("Enter the new task title: "))
        tasks[i]["title"] = new_title
        print("Task edited")
    except (IndexError, ValueError):
        print("Invalid input.")

# Main loop
while True:
    show_menu()
    choice = input("Choice an option: ")

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
        print("Exiting... See you later!")
        break
    else:
        print("Invalid option.")