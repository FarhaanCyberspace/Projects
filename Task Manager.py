import os

# Define the file to store tasks
task_file = "tasks.txt"

# Function to add a task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    with open(task_file, "a") as file:
        file.write(f"{title}, {description}\n")
    print("Task added successfully!")

# Function to list all tasks
def list_tasks():
    if os.path.exists(task_file):
        with open(task_file, "r") as file:
            tasks = file.readlines()
            if tasks:
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    title, description = task.strip().split(", ")
                    print(f"{i}. Title: {title}\n   Description: {description}")
            else:
                print("No tasks found.")
    else:
        print("No tasks found.")

# Function to update a task
def update_task():
    list_tasks()
    task_number = int(input("Enter the task number you want to update: "))
    with open(task_file, "r") as file:
        tasks = file.readlines()
    if task_number > 0 and task_number <= len(tasks):
        new_title = input("Enter new title (leave empty to keep the same): ")
        new_description = input("Enter new description (leave empty to keep the same): ")
        if not new_title:
            new_title = tasks[task_number - 1].split(", ")[0]
        if not new_description:
            new_description = tasks[task_number - 1].split(", ")[1].strip()
        tasks[task_number - 1] = f"{new_title}, {new_description}\n"
        with open(task_file, "w") as file:
            file.writelines(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    list_tasks()
    task_number = int(input("Enter the task number you want to delete: "))
    with open(task_file, "r") as file:
        tasks = file.readlines()
    if task_number > 0 and task_number <= len(tasks):
        del tasks[task_number - 1]
        with open(task_file, "w") as file:
            file.writelines(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

