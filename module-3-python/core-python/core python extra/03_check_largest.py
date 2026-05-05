#3) check a largest number(of 2 num) take num from users

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("The largest number is:", num1)
elif num2 > num1:
    print("The largest number is:", num2)
else:
    print("Both numbers are equal.")
    