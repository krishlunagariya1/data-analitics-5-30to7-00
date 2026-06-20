# =========================================================
# STUDENT ATTENDANCE MANAGEMENT SYSTEM
# Technologies Used:
# - Python
# - MySQL
# - Pandas
# =========================================================

import mysql.connector
import pandas as pd
from datetime import datetime


# MYSQL DATABASE CONNECTION
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="66511",     
    database="attendance_system"
)
cursor = conn.cursor()

# CREATE DATABASE
cursor.execute("CREATE DATABASE IF NOT EXISTS attendance_system")

cursor.execute("USE attendance_system")

#create tables
# Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no VARCHAR(50) UNIQUE NOT NULL,
    course VARCHAR(100) NOT NULL
)
""")

# Attendance Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(50) NOT NULL,
    attendance_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL
)
""")

conn.commit()

# =========================================================
# FUNCTIONS
# =========================================================

# ---------------------------------------------------------
# ADD STUDENT
# ---------------------------------------------------------

def add_student():

    print("\n========== ADD STUDENT ==========")

    name = input("Enter Student Name : ")
    roll_no = input("Enter Roll Number  : ")
    course = input("Enter Course       : ")

    try:
        sql = """
        INSERT INTO students(name, roll_no, course)
        VALUES(%s,%s,%s)
        """

        values = (name, roll_no, course)

        cursor.execute(sql, values)

        conn.commit()

        print("\n Student Added Successfully")

    except mysql.connector.Error:
        print("\n Roll Number Already Exists")


# ---------------------------------------------------------
# VIEW STUDENTS
# ---------------------------------------------------------

def view_students():

    print("\n========== STUDENT RECORDS ==========\n")

    query = "SELECT * FROM students"

    df = pd.read_sql(query, conn)

    if df.empty:
        print("No Student Records Found")

    else:
        print(df.to_string(index=False))


# ---------------------------------------------------------
# SEARCH STUDENT
# ---------------------------------------------------------

def search_student():

    roll = input("\nEnter Roll Number : ")

    query = f"""
    SELECT * FROM students
    WHERE roll_no='{roll}'
    """

    df = pd.read_sql(query, conn)

    if df.empty:
        print("\n Student Not Found")

    else:
        print("\n========== STUDENT FOUND ==========\n")
        print(df.to_string(index=False))


# ---------------------------------------------------------
# UPDATE STUDENT
# ---------------------------------------------------------

def update_student():

    roll = input("\nEnter Roll Number To Update : ")

    cursor.execute(
        "SELECT * FROM students WHERE roll_no=%s",
        (roll,)
    )

    student = cursor.fetchone()

    if student is None:
        print("\n Student Not Found")
        return

    print("\nEnter New Details")

    new_name = input("Enter New Name   : ")
    new_course = input("Enter New Course : ")

    sql = """
    UPDATE students
    SET name=%s, course=%s
    WHERE roll_no=%s
    """

    values = (new_name, new_course, roll)

    cursor.execute(sql, values)

    conn.commit()

    print("\n Student Updated Successfully")


# ---------------------------------------------------------
# DELETE STUDENT
# ---------------------------------------------------------

def delete_student():

    roll = input("\nEnter Roll Number To Delete : ")

    cursor.execute(
        "SELECT * FROM students WHERE roll_no=%s",
        (roll,)
    )

    student = cursor.fetchone()

    if student is None:
        print("\n Student Not Found")
        return

    cursor.execute(
        "DELETE FROM students WHERE roll_no=%s",
        (roll,)
    )

    conn.commit()

    print("\n Student Deleted Successfully")


# ---------------------------------------------------------
# MARK ATTENDANCE
# ---------------------------------------------------------

def mark_attendance():

    print("\n========== MARK ATTENDANCE ==========")

    roll = input("Enter Roll Number : ")

    cursor.execute(
        "SELECT * FROM students WHERE roll_no=%s",
        (roll,)
    )

    student = cursor.fetchone()

    if student is None:
        print("\n Student Not Found")
        return

    status = input("Enter Status (Present/Absent) : ")

    if status.lower() not in ["present", "absent"]:
        print("\n Invalid Attendance Status")
        return

    today = datetime.now().strftime("%Y-%m-%d")

    sql = """
    INSERT INTO attendance(roll_no, attendance_date, status)
    VALUES(%s,%s,%s)
    """

    values = (roll, today, status.capitalize())

    cursor.execute(sql, values)

    conn.commit()

    print("\n Attendance Marked Successfully")


# ---------------------------------------------------------
# VIEW ATTENDANCE
# ---------------------------------------------------------

def view_attendance():

    print("\n========== ATTENDANCE RECORDS ==========\n")

    query = """
    SELECT attendance.id,
           students.name,
           attendance.roll_no,
           students.course,
           attendance.attendance_date,
           attendance.status
    FROM attendance
    INNER JOIN students
    ON attendance.roll_no = students.roll_no
    """

    df = pd.read_sql(query, conn)

    if df.empty:
        print("No Attendance Records Found")

    else:
        print(df.to_string(index=False))


# ---------------------------------------------------------
# SEARCH ATTENDANCE BY DATE
# ---------------------------------------------------------

def search_attendance_by_date():

    date = input("\nEnter Date (YYYY-MM-DD) : ")

    query = f"""
    SELECT attendance.id,
           students.name,
           attendance.roll_no,
           attendance.attendance_date,
           attendance.status
    FROM attendance
    INNER JOIN students
    ON attendance.roll_no = students.roll_no
    WHERE attendance.attendance_date='{date}'
    """

    df = pd.read_sql(query, conn)

    if df.empty:
        print("\n No Records Found")

    else:
        print("\n========== ATTENDANCE REPORT ==========\n")
        print(df.to_string(index=False))


# ---------------------------------------------------------
# EXPORT REPORT
# ---------------------------------------------------------

def export_report():

    query = """
    SELECT attendance.id,
           students.name,
           attendance.roll_no,
           students.course,
           attendance.attendance_date,
           attendance.status
    FROM attendance
    INNER JOIN students
    ON attendance.roll_no = students.roll_no
    """

    df = pd.read_sql(query, conn)

    df.to_csv("attendance_report.csv", index=False)

    print("\n Attendance Report Exported")
    print("File Name : attendance_report.csv")


# ---------------------------------------------------------
# ATTENDANCE STATISTICS
# ---------------------------------------------------------

def attendance_statistics():

    query = """
    SELECT status, COUNT(*) AS total
    FROM attendance
    GROUP BY status
    """

    df = pd.read_sql(query, conn)

    if df.empty:
        print("\nNo Attendance Data Available")

    else:
        print("\n========== ATTENDANCE STATISTICS ==========\n")
        print(df.to_string(index=False))


# =========================================================
# MAIN MENU
# =========================================================

def menu():

    while True:

        print("\n")
        print("=" * 60)
        print("      STUDENT ATTENDANCE MANAGEMENT SYSTEM")
        print("=" * 60)

        print("""
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Mark Attendance
7. View Attendance
8. Search Attendance By Date
9. Export Attendance Report
10. Attendance Statistics
11. Exit
        """)

        choice = input("Enter Your Choice : ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            mark_attendance()

        elif choice == "7":
            view_attendance()

        elif choice == "8":
            search_attendance_by_date()

        elif choice == "9":
            export_report()

        elif choice == "10":
            attendance_statistics()

        elif choice == "11":
            print("\n Thank You For Using The System")
            break

        else:
            print("\n Invalid Choice")


# =========================================================
# START PROGRAM
# =========================================================

menu()

# =========================================================
# CLOSE DATABASE
# =========================================================

cursor.close()
conn.close()