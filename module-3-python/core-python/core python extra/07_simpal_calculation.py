'''
7) w.a.p to calcite a simple calculation take input if user select 1 preform addition 
								if 2 sum
								if 3 multi
								if 4 dive1sion
	'''

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Enter the number corresponding to the operation: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operation == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
    
