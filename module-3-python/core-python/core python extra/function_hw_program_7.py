#7.Write a program to print a year is leap year or not using number.

def leap_year():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not Leap Year")

leap_year()