# create a system to  addttion, multiplication, division, subtraction

print("1. addition")
print("2. multiplication")
print("3. division")
print("4. subtraction")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result: ", a + b)
elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result: ", a * b)
elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result: ", a / b)
elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result: ", a - b)
else:
    print("Invalid choice")
