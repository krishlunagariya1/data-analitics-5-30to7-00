# 3.Write a program to Print a factorial number.

def factorial(n):
    f = 1 
    for i in range (1, n + 1):
        f *= i
    print("Factorial:", f)

factorial(5)