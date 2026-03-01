# num=int(input("Enter a number: "))
# if num>0:
#     if num%2==0:
#         print("The number is positive and even")
#     else:
#         print("The number is positive and odd")
# else:
#     print("The number is not positive")

# wap to check a year is leap year or not tacking input from user
year=int(input("Enter a year: "))       
if (year%4==0 ): 
    if (year%100==0):
        if (year%400==0):
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")