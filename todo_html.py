import datetime
import os

def get_filename():
    today = datetime.date.today().isoformat()
    return f"todo_{today}.txt"

def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.readlines()
        print("\n📋 Today's To-do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")
    else:
        print("\n📋 No tasks yet for today.")
    return [t.strip() for t in tasks]

def add_task(filename):
    while True:
        task = input("➕ Enter a new task (or 'q' to quit): ")
        if task.lower() == 'q':
            break
        with open(filename, "a") as file:
            file.write(task + "\n")
        print("✅ Task added.")

def generate_html(tasks, filename):
    html_content = "<!DOCTYPE html>\n<html>\n<head>\n"
    html_content += "<title>Today's To-do List</title>\n</head>\n<body>\n"
    html_content += "<h1>📅 To-do List for Today</h1>\n<ul>\n"
    for task in tasks:
        html_content += f"<li>{task}</li>\n"
    html_content += "</ul>\n</body>\n</html>"

    html_filename = filename.replace(".txt", ".html")
    with open(html_filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"\n🌐 HTML file generated: {html_filename}")

def main():
    filename = get_filename()
    print(f"📅 Date: {datetime.date.today().isoformat()}")
    tasks = load_tasks(filename)
    print("\n--- Add New Tasks ---")
    add_task(filename)
    tasks = load_tasks(filename)
    generate_html(tasks, filename)
    print("\n✅ Session complete. See you next time!")

if __name__ == "__main__":
    main()
