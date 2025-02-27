import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks found!")
        return
    print("\n📌 Your To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{idx}. {task['task']} [{status}]")

# Add a new task
def add_task(tasks):
    task_desc = input("Enter task description: ")
    tasks.append({"task": task_desc, "completed": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

# Mark task as completed
def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

# Remove a task
def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed_task['task']}' removed successfully!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n📋 To-Do List Menu:")
        print("1️⃣ View Tasks")
        print("2️⃣ Add Task")
        print("3️⃣ Mark Task as Completed")
        print("4️⃣ Remove Task")
        print("5️⃣ Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
