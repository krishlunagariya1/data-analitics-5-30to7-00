# Core Python Assesment

## Question 1: Healthcare Industry

### Design a Python class ClinicAppointment that manages patient appointments in a clinic.
The system should have the following features:
### ➔ Book Appointment:
- Prompt for patient name, age, mobile number, and preferred doctor.
- Show time slots (10am, 11am, 12pm, 2pm, 3pm).
- Check slot availability and confirm booking.
### ➔ View/Cancel Appointment:
- Allow patient to view or cancel their appointment using mobile number.
### ➔ Doctor Availability:
- Maintain a maximum of 3 appointments per time slot per doctor.
### ➔ Data Persistence:
- Store appointments in memory only (no files/dbs required).


```python

class ClinicAppointment:
    def __init__(self):
        self.appointments = {}
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.max_appointments_per_slot = 3

    def book_appointment(self):
        patient_name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        mobile_number = input("Enter mobile number: ")
        preferred_doctor = input("Enter preferred doctor: ")

        print("Available time slots:")
        for slot in self.time_slots:
            print(slot)

        time_slot = input("Select a time slot: ")

        if time_slot not in self.time_slots:
            print("Invalid time slot selected.")
            return

        if self.appointments.get((preferred_doctor, time_slot), 0) >= self.max_appointments_per_slot:
            print(f"Sorry, {preferred_doctor} is fully booked at {time_slot}.")
            return

        self.appointments[(preferred_doctor, time_slot)] = self.appointments.get((preferred_doctor, time_slot), 0) + 1
        print(f"Appointment booked for {patient_name} with {preferred_doctor} at {time_slot}.")

    def view_or_cancel_appointment(self):
        mobile_number = input("Enter mobile number to view/cancel appointment: ")

        found_appointment = False
        for (doctor, slot), count in self.appointments.items():
            if count > 0:
                print(f"Appointment found: Doctor {doctor} at {slot}")
                found_appointment = True
                cancel = input("Do you want to cancel this appointment? (yes/no): ")
                if cancel.lower() == 'yes':
                    self.appointments[(doctor, slot)] -= 1
                    print("Appointment cancelled.")
                    return

        if not found_appointment:
            print("No appointment found for the given mobile number.")

clinic = ClinicAppointment()
clinic.book_appointment()
clinic.view_or_cancel_appointment()
```
Output:
```powershell
Enter patient name: Rajesh Shah
Enter patient age: 30
Enter mobile number: 1234567890
Enter preferred doctor: Dr. Rakesh
Available time slots:
10am
11am
12pm
2pm
3pm
Select a time slot: 10am
Appointment booked for Rajesh Shah with Dr. Rakesh at 10am.
Enter mobile number to view/cancel appointment: 1234567890
Appointment found: Doctor Dr. Rakesh at 10am
Do you want to cancel this appointment? (yes/no): yes
Appointment cancelled.
```


## Question 2:School Management System

### Design a Python class SchoolManagement that helps manage student admissions and records.
The system should support:
### ➔  New Admission:
-  Collect student name, age, class (1–12), and guardian's mobile number.
-  Assign a unique student ID automatically.
-  Validate age: must be between 5 and 18.
-  Validate mobile number: must be 10 digits.
### ➔  View Student Details:
-  Allow lookup using student ID.
### ➔  Update Student Info:
-  Update mobile number or class.
### ➔  Remove Student Record:
-  Remove a student using their student ID.
### ➔  Exit System

```python
class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.next_student_id = 1

    def new_admission(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        student_class = int(input("Enter class (1-12): "))
        guardian_mobile = input("Enter guardian's mobile number: ")

        if age < 5 or age > 18:
            print("Invalid age. Age must be between 5 and 18.")
            return

        if len(guardian_mobile) != 10 or not guardian_mobile.isdigit():
            print("Invalid mobile number. Mobile number must be 10 digits.")
            return

        student_id = self.next_student_id
        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "guardian_mobile": guardian_mobile
        }
        self.next_student_id += 1
        print(f"Student admitted with ID: {student_id}")

    def view_student_details(self):
        student_id = int(input("Enter student ID to view details: "))
        student = self.students.get(student_id)
        if student:
            print(f"Student ID: {student_id}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Class: {student['class']}")
            print(f"Guardian Mobile: {student['guardian_mobile']}")
        else:
            print("Student not found.")

    def update_student_info(self):
        student_id = int(input("Enter student ID to update info: "))
        student = self.students.get(student_id)
        if not student:
            print("Student not found.")
            return

        update_choice = input("What do you want to update? (mobile/class): ")
        if update_choice == "mobile":
            new_mobile = input("Enter new mobile number: ")
            if len(new_mobile) != 10 or not new_mobile.isdigit():
                print("Invalid mobile number. Mobile number must be 10 digits.")
                return
            student["guardian_mobile"] = new_mobile
            print("Mobile number updated.")
        elif update_choice == "class":
            new_class = int(input("Enter new class (1-12): "))
            if new_class < 1 or new_class > 12:
                print("Invalid class. Class must be between 1 and 12.")
                return
            student["class"] = new_class
            print("Class updated.")
        else:
            print("Invalid choice.")
    def remove_student_record(self):
        student_id = int(input("Enter student ID to remove record: "))
        if student_id in self.students:
            del self.students[student_id]
            print("Student record removed.")
        else:
            print("Student not found.")
    def exit_system(self):
        print("Exiting system. Goodbye!")
        exit()
school = SchoolManagement()
while True:
    print("\n1. New Admission")
    print("2. View Student Details")
    print("3. Update Student Info")
    print("4. Remove Student Record")
    print("5. Exit System")
    choice = input("Enter your choice: ")
    if choice == "1":
        school.new_admission()
    elif choice == "2":
        school.view_student_details()
    elif choice == "3":
        school.update_student_info()
    elif choice == "4":
        school.remove_student_record()
    elif choice == "5":
        school.exit_system()
    else:
        print("Invalid choice. Please try again.")
```
Output:
```powershell
1. New Admission
2. View Student Details
3. Update Student Info
4. Remove Student Record
5. Exit System
Enter your choice: 1
Enter student name: Alice
Enter student age: 10
Enter class (1-12): 5
Enter guardian's mobile number: 1234567890
Student admitted with ID: 1
1. New Admission
2. View Student Details
3. Update Student Info
4. Remove Student Record
5. Exit System
Enter your choice: 2
Enter student ID to view details: 1
Student ID: 1
Name: Brijesh
Age: 21
Class: 12
Guardian Mobile: 1234567890
1. New Admission
2. View Student Details
3. Update Student Info
4. Remove Student Record
5. Exit System
Enter your choice: 3
Enter student ID to update info: 1
What do you want to update? (mobile/class): mobile
Enter new mobile number: 0987654321
Mobile number updated.
1. New Admission
2. View Student Details
3. Update Student Info
4. Remove Student Record
5. Exit System
Enter your choice: 4
Enter student ID to remove record: 1
Student record removed.
1. New Admission
2. View Student Details
3. Update Student Info
4. Remove Student Record
5. Exit System
Enter your choice: 5
Exiting system. Goodbye!
```

## Transport Reservation System (Bus Ticketing)

### Design a Python class BusReservation that simulates a basic bus ticket booking system.
Features should include:
### ➔  Show Available Routes:
-  Predefined city routes with fixed prices.
-  Example: "Mumbai to Pune - ₹500", "Delhi to Jaipur - ₹600", etc.
### ➔  Book Ticket:
-  Enter passenger name, age, mobile, and route.
-  Assign seat number (max 40 per bus per route).
-  Generate a unique ticket ID.
### ➔  View Ticket:
-  Lookup using ticket ID.
### ➔  Cancel Ticket:
-  Cancel the ticket if it exists.
### ➔  Exit

```python
class BusReservation:
    def __init__(self):
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 400
        }
        self.tickets = {}
        self.next_ticket_id = 1
        self.max_seats_per_route = 40

    def show_available_routes(self):
        print("Available Routes:")
        for route, price in self.routes.items():
            print(f"{route} - ₹{price}")

    def book_ticket(self):
        passenger_name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        mobile_number = input("Enter mobile number: ")
        route = input("Enter route: ")

        if route not in self.routes:
            print("Invalid route selected.")
            return

        if len(mobile_number) != 10 or not mobile_number.isdigit():
            print("Invalid mobile number. Mobile number must be 10 digits.")
            return

        if sum(1 for ticket in self.tickets.values() if ticket['route'] == route) >= self.max_seats_per_route:
            print(f"Sorry, no seats available for {route}.")
            return

        ticket_id = self.next_ticket_id
        seat_number = sum(1 for ticket in self.tickets.values() if ticket['route'] == route) + 1
        self.tickets[ticket_id] = {
            "passenger_name": passenger_name,
            "age": age,
            "mobile_number": mobile_number,
            "route": route,
            "seat_number": seat_number
        }
        self.next_ticket_id += 1
        print(f"Ticket booked successfully! Ticket ID: {ticket_id}, Seat Number: {seat_number}")

    def view_ticket(self):
        ticket_id = int(input("Enter ticket ID to view details: "))
        ticket = self.tickets.get(ticket_id)
        if ticket:
            print(f"Ticket ID: {ticket_id}")
            print(f"Passenger Name: {ticket['passenger_name']}")
            print(f"Age: {ticket['age']}")
            print(f"Mobile Number: {ticket['mobile_number']}")
            print(f"Route: {ticket['route']}")
            print(f"Seat Number: {ticket['seat_number']}")
        else:
            print("Ticket not found.")

    def cancel_ticket(self):
        ticket_id = int(input("Enter ticket ID to cancel: "))
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]
            print("Ticket cancelled successfully.")
        else:
            print("Ticket not found.")
    def exit_system(self):
        print("Exiting system. Goodbye!")
        exit()
bus_reservation = BusReservation()
while True:
    print("\n1. Show Available Routes")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        bus_reservation.show_available_routes()
    elif choice == "2":
        bus_reservation.book_ticket()
    elif choice == "3":
        bus_reservation.view_ticket()
    elif choice == "4":
        bus_reservation.cancel_ticket()
    elif choice == "5":
        bus_reservation.exit_system()
    else:
        print("Invalid choice. Please try again.")
```

Output:
```powershell
1. Show Available Routes
2. Book Ticket
3. View Ticket
4. Cancel Ticket
5. Exit
Enter your choice: 1
Available Routes:
Mumbai to Pune - ₹500
Delhi to Jaipur - ₹600
Bangalore to Chennai - ₹400
1. Show Available Routes
2. Book Ticket
3. View Ticket
4. Cancel Ticket
5. Exit
Enter your choice: 2
Enter passenger name: John Doe
Enter passenger age: 25
Enter mobile number: 1234567890
Enter route: Mumbai to Pune
Ticket booked successfully! Ticket ID: 1, Seat Number: 1
1. Show Available Routes
2. Book Ticket
3. View Ticket
4. Cancel Ticket
5. Exit
Enter your choice: 3
Enter ticket ID to view details: 1
Ticket ID: 1
Passenger Name: John Doe
Age: 25
Mobile Number: 1234567890
Route: Mumbai to Pune
Seat Number: 1
1. Show Available Routes
2. Book Ticket
3. View Ticket
4. Cancel Ticket
5. Exit
Enter your choice: 4
Enter ticket ID to cancel: 1
Ticket cancelled successfully.
1. Show Available Routes
2. Book Ticket
3. View Ticket
4. Cancel Ticket
5. Exit
Enter your choice: 5
Exiting system. Goodbye!
```