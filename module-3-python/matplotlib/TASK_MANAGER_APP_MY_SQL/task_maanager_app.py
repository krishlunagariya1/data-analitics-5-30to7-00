# create a database connection mysql 
# create a pandas for data set or data frames 
# create a matplotlib for data visualisation in chart
# install all ....
# pip install pandas matplotlib mysql-connector-python 

# create an app and import all dependancies
import pandas as pd 
import matplotlib.pyplot as plt 
import mysql.connector
# database connection 
db=mysql.connector.connect(
    
    host="localhost",
    user="root", 
    password="66511",
    database="task_manager_appdb"
)

cursor=db.cursor();
print("connection successfully stablished")


#create a function
def add_task():
    task_name = input("Enter task name: ")
    priority = input("Enter your task priority: ")
    status = input("Enter your task status: ")

    sql = """
    insert into tasks (task_name,priority,status) 
    values (%s,%s,%s)
    """
    values = (task_name,priority,status)
    cursor.execute(sql,values)
    db.commit()
    print("task added successfully")

#display tasks
def display_tasks():
    sql = "select * from tasks"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("\n ============display all tasks ============")
    for row in result:
        print(row)

#update task
def update_task():
    task_id = input("Enter task id to update: ")
    new_status = input("Enter new status: ")

    sql = "update tasks set status=%s where id=%s"
    values = (new_status, task_id)
    cursor.execute(sql, values)
    db.commit()
    print("task updated successfully")

#delete task
def delete_task():
    task_id = input("Enter task id to delete: ")

    sql = "delete from tasks where id=%s"
    values = (task_id,)
    cursor.execute(sql, values)
    db.commit()
    print("task deleted successfully")

# show task in chart
def show_task_chart():
    sql = "select status, count(*) from tasks group by status"
    cursor.execute(sql)
    result = cursor.fetchall()

    statuses = [row[0] for row in result]
    counts = [row[1] for row in result]

    plt.pie(counts, labels=statuses, autopct='%1.1f%%')
    plt.title("Task Status Distribution")
    plt.show()

# show task in bar chart
def show_task_bar_chart():
    sql = "select priority, count(*) from tasks group by priority"
    cursor.execute(sql)
    result = cursor.fetchall()

    priorities = [row[0] for row in result]
    counts = [row[1] for row in result]

    plt.bar(priorities, counts)
    plt.xlabel("Priority")
    plt.ylabel("Count")
    plt.title("Task Priority Distribution")
    plt.show()


while True:
    print(""" ====task manager app====
    1. Add task
    2. desplay tasks
    3. update task
    4. delete task
    5. show task in chart
    6. show task in bar chart
    7. exit   
          """)
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        show_task_chart()
    elif choice == "6":
        show_task_bar_chart()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")