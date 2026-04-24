# Core Oython Assesment

## Question 1: Healthcare Industry

### Design a Python class ClinicAppointment that manages patient appointments in a clinic.
The system should have the following features:
➔ Book Appointment:
● Prompt for patient name, age, mobile number, and preferred doctor.
● Show time slots (10am, 11am, 12pm, 2pm, 3pm).
● Check slot availability and confirm booking.
➔ View/Cancel Appointment:
● Allow patient to view or cancel their appointment using mobile number.
➔ Doctor Availability:
● Maintain a maximum of 3 appointments per time slot per doctor.
➔ Data Persistence:
● Store appointments in memory only (no files/dbs required).


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
Enter patient name: John Doe
Enter patient age: 30
Enter mobile number: 1234567890
Enter preferred doctor: Dr. Smith
Available time slots:
10am
11am
12pm
2pm
3pm
Select a time slot: 10am
Appointment booked for John Doe with Dr. Smith at 10am.
Enter mobile number to view/cancel appointment: 1234567890
Appointment found: Doctor Dr. Smith at 10am
Do you want to cancel this appointment? (yes/no): yes
Appointment cancelled.
```


## Question 2:School Management System

### Design a Python class SchoolManagement that helps manage student admissions and records. 
The system should support:
➔  New Admission:
●  Collect student name, age, class (1–12), and guardian's mobile number.
●  Assign a unique student ID automatically.
●  Validate age: must be between 5 and 18.
●  Validate mobile number: must be 10 digits.
➔  View Student Details:
●  Allow lookup using student ID.
➔  Update Student Info:
●  Update mobile number or class.
➔  Remove Student Record:
●  Remove a student using their student ID.
➔  Exit System