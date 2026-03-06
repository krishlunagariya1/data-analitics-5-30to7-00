#6) wap to swap to number using 3rd variable and without using 3rd variable 

# using 3rd variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = a
a = b
b = temp
print("After swapping:")
print("First number:", a)
print("Second number:", b)

# without using 3rd variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("First number:", a)
print("Second number:", b)
