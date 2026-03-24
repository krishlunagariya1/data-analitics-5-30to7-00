#1. Write a function to print your name and age.

def my_info():
    print("My name is krish and I am 20 years old.")
#output: My name is krish and I am 20 years old.


#2. Create a function that prints numbers from 1 to 10.

def print_numbers():
    for i in range (1, 11):
        print(i)
#output: 1 2 3 4 5 6 7 8 9 10

#3. Write a function to check whether a number is even or odd

def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
#output: check_even_odd(4) -> Even
#output: check_even_odd(7) -> Odd


#4. Create a function that takes a number and prints its square.

def square(n):
    print(n * n)
#output: square(5) -> 25


#5. Write a function to print a multiplication table of a given number.

def table(n):
    for i in range(1, 11):
        print(n * i)


     