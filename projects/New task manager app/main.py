import sqlite3
import matplotlib.pyplot as plt

# Database Connection
conn = sqlite3.connect("task_manager.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
)
""")
conn.commit()


# Add Task
def add_task():
    task = input("Enter Task Name : ")

    cursor.execute(
        "INSERT INTO tasks(task_name) VALUES(?)",
        (task,)
    )
    conn.commit()

    print("Task Added Successfully.")


# Display Tasks
def display_tasks():
    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()

    if len(data) == 0:
        print("No Tasks Found.")
        return

    print("\n------ TASK LIST ------")
    print("ID\tTask\t\tStatus")

    for row in data:
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}")


# Update Task
def update_task():
    display_tasks()

    task_id = int(input("\nEnter Task ID to Update : "))

    cursor.execute(
        "SELECT * FROM tasks WHERE id=?",
        (task_id,)
    )

    task = cursor.fetchone()

    if task is None:
        print("Task Not Found.")
        return

    print("\n1. Change Task Name")
    print("2. Change Status")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        new_task = input("Enter New Task Name : ")

        cursor.execute(
            "UPDATE tasks SET task_name=? WHERE id=?",
            (new_task, task_id)
        )
        conn.commit()

        print("Task Updated Successfully.")

    elif choice == 2:
        print("\n1. Pending")
        print("2. Completed")

        status_choice = int(input("Enter Choice : "))

        if status_choice == 1:
            status = "Pending"
        elif status_choice == 2:
            status = "Completed"
        else:
            print("Invalid Choice")
            return

        cursor.execute(
            "UPDATE tasks SET status=? WHERE id=?",
            (status, task_id)
        )
        conn.commit()

        print("Status Updated Successfully.")

    else:
        print("Invalid Choice.")


# Delete Task
def delete_task():
    display_tasks()

    task_id = int(input("\nEnter Task ID to Delete : ")

)
    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )
    conn.commit()

    print("Task Deleted Successfully.")


# Pie Chart
def show_chart():
    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE status='Completed'"
    )
    completed = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE status='Pending'"
    )
    pending = cursor.fetchone()[0]

    if completed == 0 and pending == 0:
        print("No Tasks Available.")
        return

    labels = ["Completed", "Pending"]
    values = [completed, pending]

    plt.figure(figsize=(6, 6))
    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )
    plt.title("Task Status Ratio")
    plt.show()


# Main Menu
while True:
    print("\n====== TASK MANAGER ======")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Edit and Update Task")
    print("4. Delete Task")
    print("5. Show Pie Chart")
    print("6. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        add_task()

    elif choice == 2:
        display_tasks()

    elif choice == 3:
        update_task()

    elif choice == 4:
        delete_task()

    elif choice == 5:
        show_chart()

    elif choice == 6:
        print("Thank You...")
        conn.close()
        break

    else:
        print("Invalid Choice.")