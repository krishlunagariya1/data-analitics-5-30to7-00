# Employee Management System (Python + Tkinter + MySQL)

A desktop app to manage employee records — add, update, delete,
search, and view employees in a table — backed by a MySQL database.

## Project Structure
```
employee-management-system/
├── main.py         # Tkinter GUI (forms, table, buttons)
├── database.py     # MySQL database logic (CRUD functions)
├── config.py       # MySQL connection settings (edit this!)
└── README.md
```

## Requirements
- Python 3.8+
- MySQL Server installed and **running** (MySQL 5.7+ / 8.x, or MariaDB)
- `mysql-connector-python` driver

### 1. Install the MySQL driver
```bash
pip install mysql-connector-python
```

### 2. Configure your MySQL credentials
Open `config.py` and set your actual MySQL username/password:
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_mysql_password",   # <-- change this
    "port": 3306,
}
```
You do **not** need to manually create the database or table — the app
creates the `employee_management` database and `employees` table
automatically on first run (`CREATE DATABASE IF NOT EXISTS`, `CREATE TABLE
IF NOT EXISTS`).

### 3. Run the app
```bash
python main.py
```

If MySQL isn't running or the credentials are wrong, you'll get a clear
popup error instead of a crash — check `config.py` and confirm MySQL is
running (`mysql -u root -p` should connect from your terminal).

## Features
- **Add**: Fill the form, click "Add Employee"
- **Update**: Click a row in the table (auto-fills the form), edit fields, click "Update Selected"
- **Delete**: Click a row, click "Delete Selected"
- **Search**: Type in the search box — filters by name, department, or designation live

## Database Schema
```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    designation VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    joining_date VARCHAR(20)
);
```

## How to Extend This Into a Full System
1. **Login/Authentication** — add a `users` table + a login screen (admin/HR roles)
2. **Attendance module** — new table `attendance(emp_id, date, status)` with a
   calendar-style UI and monthly reports
3. **Salary/Payroll** — bonuses, deductions, generate payslips (e.g. with `reportlab` for PDF)
4. **Departments as their own table** — a `departments` table + a dropdown
   (`ttk.Combobox`) instead of free-text department entry, with a foreign key
5. **Export to Excel/CSV** — use `pandas` or the `csv` module
6. **Move to a web app** — port this to Flask/Django using the same MySQL
   database, so multiple people can access it via browser
7. **Connection pooling** — for a multi-user app, use
   `mysql.connector.pooling.MySQLConnectionPool` instead of opening a new
   connection per query

