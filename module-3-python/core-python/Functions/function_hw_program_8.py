# 8.Write a program to print compound interest using function. 

def compound_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate: "))
    t = float(input("Enter time: "))
    
    amount = p * (1 + r/100) ** t
    ci = amount - p
    
    print("Compound Interest:", ci)

compound_interest()