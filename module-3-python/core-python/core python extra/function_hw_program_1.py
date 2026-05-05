#1.Write a program to check a number is prime number or not using number.

def is_prime(n):
    if n < 2:
        print("Not Prime")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime")

# Example
is_prime(5)