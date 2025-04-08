tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    print("To-do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def run_tests():
    tasks.clear()
    add_task("Test Task")
    assert "Test Task" in tasks, "add_task failed"

    tasks.clear()
    add_task("Task A")
    add_task("Task B")
    assert len(tasks) == 2, "show_tasks length mismatch"

    print("✅ All tests passed.")

if __name__ == "__main__":
    print("1. Run Program")
    print("2. Run Tests")
    choice = input("Select an option (1/2): ")

    if choice == "1":
        add_task("Study Git")
        add_task("Write a report")
        add_task("Push to GitHub")
        show_tasks()
    elif choice == "2":
        run_tests()
    else:
        print("Invalid option.")
