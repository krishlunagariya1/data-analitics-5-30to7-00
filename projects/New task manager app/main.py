import pandas as pd
import matplotlib.pyplot as plt
import os

# Create CSV file if it doesn't exist
if not os.path.exists("tasks.csv"):
    df = pd.DataFrame(columns=["id", "title", "priority", "status"])
    df.to_csv("tasks.csv", index=False)

print("Task Manager Started Successfully")


# Load DataFrame
def load_df():
    return pd.read_csv("tasks.csv")


# Save DataFrame
def save_df(df):
    df.to_csv("tasks.csv", index=False)


# Add Task
def add_task():
    df = load_df()

    title = input("Enter task Name: ")
    priority = input("Enter task Priority: ")
    status = input("Enter task Status: ")

    if len(df) == 0:
        task_id = 1
    else:
        task_id = df["id"].max() + 1

    new_task = pd.DataFrame({
        "id": [task_id],
        "title": [title],
        "priority": [priority],
        "status": [status]
    })

    df = pd.concat([df, new_task], ignore_index=True)
    save_df(df)

    print("Task Successfully Added")


# Display Task
def display_task():
    df = load_df()
    print("\n========== DISPLAY TASKS ==========")

    if df.empty:
        print("No tasks found.")
    else:
        print(df)


# Update Task
def update_task():
    df = load_df()

    taskid = int(input("Enter Task ID to Update: "))

    if taskid not in df["id"].values:
        print("Task ID not found.")
        return

    title = input("Enter New Task Name: ")
    priority = input("Enter New Priority: ")
    status = input("Enter New Status: ")

    df.loc[df["id"] == taskid, "title"] = title
    df.loc[df["id"] == taskid, "priority"] = priority
    df.loc[df["id"] == taskid, "status"] = status

    save_df(df)
    print("Task Successfully Updated")


# Delete Task
def delete_task():
    df = load_df()

    taskid = int(input("Enter Task ID to Delete: "))

    if taskid not in df["id"].values:
        print("Task ID not found.")
        return

    df = df[df["id"] != taskid]
    save_df(df)

    print("Task Successfully Deleted")


# Pie Chart
def showpiechart():
    df = load_df()

    if df.empty:
        print("No data available.")
        return

    status_count = df["status"].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(
        status_count,
        labels=status_count.index,
        autopct="%1.1f%%"
    )
    plt.title("Task Status Pie Chart")
    plt.show()


# Bar Chart
def showbarchart():
    df = load_df()

    if df.empty:
        print("No data available.")
        return

    status_count = df["status"].value_counts()

    plt.figure(figsize=(7, 5))
    plt.bar(
        status_count.index,
        status_count.values
    )
    plt.title("Task Status Bar Chart")
    plt.xlabel("Status")
    plt.ylabel("Number of Tasks")
    plt.show()


# Main Menu
while True:
    print("""
===== TASK MANAGER APP =====
1. Add Task
2. Display Task
3. Update Task
4. Delete Task
5. Show Pie Chart
6. Show Bar Chart
7. Exit
""")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        display_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        showpiechart()
    elif choice == "6":
        showbarchart()
    elif choice == "7":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")