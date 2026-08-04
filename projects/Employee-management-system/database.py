"""
database.py
------------
Handles all MySQL database operations for the Employee Management System,
using the official `mysql-connector-python` driver.

Install the driver first:
    pip install mysql-connector-python
"""

import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG, DB_NAME


def get_connection():
    """Return a new connection to the employee_management MySQL database."""
    return mysql.connector.connect(database=DB_NAME, **DB_CONFIG)


def create_database_and_table():
    """
    Create the database (if it doesn't exist) and the employees table.
    Run once at app startup — safe to call every time since it uses
    CREATE ... IF NOT EXISTS.
    """
    # Step 1: connect without selecting a database, to create it if missing
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.commit()
    cursor.close()
    conn.close()

    # Step 2: connect to the database and create the table
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            department VARCHAR(100) NOT NULL,
            designation VARCHAR(100) NOT NULL,
            salary DECIMAL(10, 2) NOT NULL,
            phone VARCHAR(20),
            email VARCHAR(100),
            joining_date VARCHAR(20)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


def add_employee(name, department, designation, salary, phone, email, joining_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees (name, department, designation, salary, phone, email, joining_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (name, department, designation, salary, phone, email, joining_date))
    conn.commit()
    cursor.close()
    conn.close()


def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees ORDER BY id")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def search_employees(keyword):
    """Search by name, department, or designation (case-insensitive)."""
    conn = get_connection()
    cursor = conn.cursor()
    like = f"%{keyword}%"
    cursor.execute("""
        SELECT * FROM employees
        WHERE name LIKE %s OR department LIKE %s OR designation LIKE %s
        ORDER BY id
    """, (like, like, like))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def update_employee(emp_id, name, department, designation, salary, phone, email, joining_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE employees
        SET name = %s, department = %s, designation = %s, salary = %s,
            phone = %s, email = %s, joining_date = %s
        WHERE id = %s
    """, (name, department, designation, salary, phone, email, joining_date, emp_id))
    conn.commit()
    cursor.close()
    conn.close()


def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (emp_id,))
    conn.commit()
    cursor.close()
    conn.close()
