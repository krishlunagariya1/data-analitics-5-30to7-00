"""
main.py
--------
Employee Management System - Tkinter Desktop App
Run with: python main.py

Features:
- Add / Update / Delete employee records
- View all employees in a table (Treeview)
- Search by name, department, or designation
- Data persisted in a local SQLite database (employees.db)
"""

import tkinter as tk
from tkinter import ttk, messagebox
from mysql.connector import Error as MySQLError
import database as db


class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("950x600")
        self.root.configure(bg="#f0f2f5")

        self.selected_id = None  # Tracks which row is selected for update/delete

        try:
            db.create_database_and_table()
        except MySQLError as e:
            messagebox.showerror(
                "Database Connection Failed",
                f"Could not connect to MySQL.\n\nCheck config.py (host/user/password) "
                f"and make sure MySQL is running.\n\nDetails: {e}"
            )
            root.destroy()
            return

        self.build_form()
        self.build_table()
        self.build_buttons()
        self.load_table_data()

    # ---------------- FORM ----------------
    def build_form(self):
        form_frame = tk.LabelFrame(self.root, text="Employee Details", bg="#f0f2f5",
                                    font=("Segoe UI", 10, "bold"), padx=15, pady=15)
        form_frame.place(x=15, y=15, width=920, height=160)

        labels = ["Name", "Department", "Designation", "Salary",
                  "Phone", "Email", "Joining Date (YYYY-MM-DD)"]
        self.entries = {}

        for i, label in enumerate(labels):
            row, col = divmod(i, 4)
            tk.Label(form_frame, text=label, bg="#f0f2f5",
                     font=("Segoe UI", 9)).grid(row=row * 2, column=col, sticky="w", padx=8, pady=(5, 0))
            entry = tk.Entry(form_frame, width=22)
            entry.grid(row=row * 2 + 1, column=col, padx=8, pady=(0, 8))
            self.entries[label] = entry

    def get_entry(self, label):
        return self.entries[label].get().strip()

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.selected_id = None
        self.table.selection_remove(self.table.selection())

    # ---------------- BUTTONS ----------------
    def build_buttons(self):
        btn_frame = tk.Frame(self.root, bg="#f0f2f5")
        btn_frame.place(x=15, y=185, width=920, height=40)

        buttons = [
            ("Add Employee", "#2e7d32", self.add_employee),
            ("Update Selected", "#1565c0", self.update_employee),
            ("Delete Selected", "#c62828", self.delete_employee),
            ("Clear Form", "#616161", self.clear_form),
        ]
        for i, (text, color, cmd) in enumerate(buttons):
            tk.Button(btn_frame, text=text, bg=color, fg="white", width=18,
                      font=("Segoe UI", 9, "bold"), command=cmd).grid(row=0, column=i, padx=6)

        # Search bar
        search_frame = tk.Frame(self.root, bg="#f0f2f5")
        search_frame.place(x=15, y=230, width=920, height=35)
        tk.Label(search_frame, text="Search:", bg="#f0f2f5").pack(side="left", padx=(0, 5))
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.load_table_data())
        tk.Entry(search_frame, textvariable=self.search_var, width=40).pack(side="left")

    # ---------------- TABLE ----------------
    def build_table(self):
        columns = ("ID", "Name", "Department", "Designation", "Salary", "Phone", "Email", "Joining Date")
        self.table = ttk.Treeview(self.root, columns=columns, show="headings", height=15)

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=105, anchor="center")
        self.table.column("Email", width=150)

        self.table.place(x=15, y=275, width=920, height=310)
        self.table.bind("<<TreeviewSelect>>", self.on_row_select)

    def load_table_data(self):
        for row in self.table.get_children():
            self.table.delete(row)

        keyword = self.search_var.get().strip()
        try:
            rows = db.search_employees(keyword) if keyword else db.get_all_employees()
        except MySQLError as e:
            messagebox.showerror("Database Error", str(e))
            return
        for row in rows:
            self.table.insert("", tk.END, values=row)

    def on_row_select(self, event):
        selected = self.table.selection()
        if not selected:
            return
        values = self.table.item(selected[0])["values"]
        self.selected_id = values[0]

        labels = ["Name", "Department", "Designation", "Salary",
                  "Phone", "Email", "Joining Date (YYYY-MM-DD)"]
        for label, value in zip(labels, values[1:]):
            self.entries[label].delete(0, tk.END)
            self.entries[label].insert(0, value)

    # ---------------- CRUD ACTIONS ----------------
    def validate_form(self):
        name = self.get_entry("Name")
        department = self.get_entry("Department")
        designation = self.get_entry("Designation")
        salary = self.get_entry("Salary")

        if not name or not department or not designation or not salary:
            messagebox.showwarning("Missing Data", "Name, Department, Designation, and Salary are required.")
            return None
        try:
            salary = float(salary)
        except ValueError:
            messagebox.showwarning("Invalid Data", "Salary must be a number.")
            return None
        return name, department, designation, salary

    def add_employee(self):
        result = self.validate_form()
        if not result:
            return
        name, department, designation, salary = result
        phone = self.get_entry("Phone")
        email = self.get_entry("Email")
        joining_date = self.get_entry("Joining Date (YYYY-MM-DD)")

        try:
            db.add_employee(name, department, designation, salary, phone, email, joining_date)
        except MySQLError as e:
            messagebox.showerror("Database Error", str(e))
            return
        messagebox.showinfo("Success", "Employee added successfully.")
        self.clear_form()
        self.load_table_data()

    def update_employee(self):
        if self.selected_id is None:
            messagebox.showwarning("No Selection", "Select an employee from the table to update.")
            return
        result = self.validate_form()
        if not result:
            return
        name, department, designation, salary = result
        phone = self.get_entry("Phone")
        email = self.get_entry("Email")
        joining_date = self.get_entry("Joining Date (YYYY-MM-DD)")

        try:
            db.update_employee(self.selected_id, name, department, designation,
                                salary, phone, email, joining_date)
        except MySQLError as e:
            messagebox.showerror("Database Error", str(e))
            return
        messagebox.showinfo("Success", "Employee updated successfully.")
        self.clear_form()
        self.load_table_data()

    def delete_employee(self):
        if self.selected_id is None:
            messagebox.showwarning("No Selection", "Select an employee from the table to delete.")
            return
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this employee?")
        if confirm:
            try:
                db.delete_employee(self.selected_id)
            except MySQLError as e:
                messagebox.showerror("Database Error", str(e))
                return
            messagebox.showinfo("Deleted", "Employee deleted successfully.")
            self.clear_form()
            self.load_table_data()


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()
