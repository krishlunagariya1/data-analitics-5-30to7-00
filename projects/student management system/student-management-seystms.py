import os
file_name="students.txt"
# if file does not exist create a file 
if not os.path.exists(file_name):
    open(file_name,'w').close()
# add students data
def add_student():
    name=input("Enter your name :")
    age=input("Enter your age :")
    rollnumber=input("Enter your roll numbers :")
    grade=input("Enter your grade :")
    course=input("Enter your course :")
    
    with open(file_name,'a') as f:
        f.write(f"{name} , {age} , {rollnumber} ,{grade} , {course} \n")
    print("🆗 Students added successfully")
   
# views students data
def view_student():
    with open(file_name,'r') as f:
        viewstudents=f.readlines()
        print("-----views students records------")
        for i in viewstudents:
            name,age,rollnumber,grade,course=i.strip().split(',')
            print(f"Name :{name}, Age : {age}, Roll Numbers : {rollnumber} , Grade : {grade} , Course  : {course} ")
    
# search students
def search_student():
    rollnumber=input("Enter your roll number to search :")
    with open(file_name,'r') as f:
        viewstudents=f.readlines()
        print("-----search students records------")
        for i in viewstudents:
            name,age,rollnumber1,grade,course=i.strip().split(',')
            if rollnumber1==rollnumber:
                print(f"Name :{name}, Age : {age}, Roll Numbers : {rollnumber1} , Grade : {grade} , Course  : {course} ")
                break
        else:
            print("🙄 student record not found")
# update students data
def update_student():
    rollnumber=input("Enter your roll number to update :")
    with open(file_name,'r') as f:
        viewstudents=f.readlines()
    with open(file_name,'w') as f:
        for i in viewstudents:
            name,age,rollnumber1,grade,course=i.strip().split(',')
            if rollnumber1==rollnumber:
                print(f"Name :{name}, Age : {age}, Roll Numbers : {rollnumber1} , Grade : {grade} , Course  : {course} ")
                name=input("Enter your name :")
                age=input("Enter your age :")
                grade=input("Enter your grade :")
                course=input("Enter your course :")
                f.write(f"{name} , {age} , {rollnumber} ,{grade} , {course} \n")
            else:
                f.write(i)
    print("🆗 Students updated successfully")

# delete students data
def delete_student():
    rollnumber=input("Enter your roll number to delete :")
    with open(file_name,'r') as f:
        viewstudents=f.readlines()
    with open(file_name,'w') as f:
        for i in viewstudents:
            name,age,rollnumber1,grade,course=i.strip().split(',')
            if rollnumber1!=rollnumber:
                f.write(i)
    print("🆗 Students deleted successfully")

# create a CLI menu
def menu():
    while True:
        print("\n 👤------students manage systems app-----😀")
        print("1. Add students")
        print("2. View students")
        print("3. Search students")
        print("4. update students")
        print("5. delete students")
        print("6. Exit")
        # select choice to perform actions 
        choice=input("Enter your choice to perform actions :")
        if choice=='1':
            add_student()
        elif choice=='2':
            view_student()
        elif choice=='3':
            search_student()
        elif choice=='4':
            update_student()
        elif choice=='5':
            delete_student()
        elif choice=='6':
            print('🧤 thanks to used our app')     
            break 
        else:
            print("🙄 invalid choice selected try again")              
            
            
        
#call a function 
menu() 
  