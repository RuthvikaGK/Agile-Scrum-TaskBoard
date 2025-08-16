# Agile Scrum Task Board Mini Project

scrum_board = {
    "Backlog": [],
    "In Progress": [],
    "Done": []
}

def show_board():
    print("\n=== Scrum Board ===")
    for stage, tasks in scrum_board.items():
        print(f"{stage}: {', '.join(tasks) if tasks else 'No tasks'}")
    print("===================")

def add_task():
    task = input("Enter task name: ")
    scrum_board["Backlog"].append(task)
    print(f"✅ Task '{task}' added to Backlog")

def move_task():
    show_board()
    task = input("Enter task name to move: ")
    for stage, tasks in scrum_board.items():
        if task in tasks:
            if stage == "Backlog":
                scrum_board["Backlog"].remove(task)
                scrum_board["In Progress"].append(task)
                print(f"🚀 Task '{task}' moved to In Progress")
                return
            elif stage == "In Progress":
                scrum_board["In Progress"].remove(task)
                scrum_board["Done"].append(task)
                print(f"🎉 Task '{task}' moved to Done")
                return
            elif stage == "Done":
                print(f"⚡ Task '{task}' is already in Done")
                return
    print("❌ Task not found!")

def menu():
    while True:   # 🔁 Infinite loop until Exit
        print("\n--- Scrum Board Menu ---")
        print("1. Add Task (Backlog)")
        print("2. Move Task (Next Stage)")
        print("3. Show Board")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            move_task()
        elif choice == "3":
            show_board()
        elif choice == "4":
            print("Exiting Scrum Board... 👋")
            break
        else:
            print("Invalid choice! Try again.")

# Run the menu
menu()
