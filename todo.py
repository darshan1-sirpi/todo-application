# To-Do App with File Storage (Single Script)

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

def view_tasks(tasks):
    if not tasks:
        print("⚠️ No tasks found.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"🗑️ Deleted: {removed}")
            else:
                print("❌ Invalid number")
        except:
            print("❌ Enter valid number")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice")

# Run app
if __name__ == "__main__":
    main()
    #helooo 
