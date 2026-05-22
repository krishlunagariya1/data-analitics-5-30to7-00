#what are operators in python?
# Operators are special symbols or keywords that perform specific operations on one or more operands (values or variables). 
# They are used to manipulate data and perform various computations in Python.
# There are several types of operators in Python, including:
# 1. Arithmetic Operators: These operators perform basic mathematical operations such as addition (+), subtraction (-), multiplication (*), division (/), floor division (//), modulus (%), and exponentiation (**).
# 2. Comparison Operators: These operators compare two values and return a boolean result (True or False). Examples include equal to (==), not equal to (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).
# 3. Logical Operators: These operators are used to combine multiple boolean expressions. They include and (and), or (or), and not (not).
# 4. Assignment Operators: These operators are used to assign values to variables. Examples include the simple assignment operator (=), as well as compound assignment operators like +=, -=, *=, /=, etc.      
                    

a = 10 
b = 3

# arithmetic operators
print(a+b)
#output: 13
print(a-b)
#output: 7
print(a*b)
#output: 30
print(a/b)  # this will give you the quotient of a divided by b
#output: 3.3333333333333335
print(a//b)  # this will give you the floor division result of a divided by b, which is the largest integer less than or equal to the quotient
#output: 3
print(a%b)  # this will give you the remainder of a divided by b
#output: 1
print(a**b)  # this will give you a raised to the power of b, which is 10 raised to the power of 3, resulting in 1000
#output: 1000

# comparison operators
print(a == b)  # this will check if a is equal to b, which is False
#output: False
print(a != b)  # this will check if a is not equal to b, which is True
#output: True
print(a > b)  # this will check if a is greater than b, which is True
#output: True
print(a < b)  # this will check if a is less than b, which is False
#output: False
print(a >= b)  # this will check if a is greater than or equal to b
#output: True
print(a <= b)  # this will check if a is less than or equal to b, which is False
#output: False

# logical operators
x = True
y = False
print(x and y)  # this will return True if both x and y are True, which is False
#output: False
print(x or y)  # this will return True if at least one of x or y is True, which is True
#output: True
print(not x)  # this will return the opposite of x, which is False
#output: False

# assignment operators
c = 5
c += 2  # this is equivalent to c = c + 2, which will update the value of c to 7
print(c)  # this will print the updated value of c, which is 7
#output: 7
c *= 3  # this is equivalent to c = c * 3, which will update the value of c to 21
print(c)  # this will print the updated value of c, which is 21
#output: 21

#bitwise operators
d = 5  # in binary: 0101
e = 3  # in binary: 0011
print(d & e)  # this will perform a bitwise AND operation, resulting in 1 (in binary: 0001)
#output: 1
print(d | e)  # this will perform a bitwise OR operation, resulting in 7 (in binary: 0111)
#output: 7
print(d ^ e)  # this will perform a bitwise XOR operation, resulting in 6 (in binary: 0110)
#output: 6
print(~d)  # this will perform a bitwise NOT operation, resulting in -6
#output: -6
print(d << 1)  # this will perform a left shift operation, resulting in 10 (in binary: 1010)
#output: 10
print(d >> 1)  # this will perform a right shift operation, resulting in 2 (in binary: 0010)
#output: 2

#membership operators
list1 = [1, 2, 3, 4, 5]
print(3 in list1)  # this will check if 3 is present in list
#output: True
print(6 in list1)  # this will check if 6 is present in list
#output: False
print(3 not in list1)  # this will check if 3 is not present in list
#output: False
print(6 not in list1)  # this will check if 6 is not present in list
#output: True

#identity operators
f = [1, 2, 3]
g = f  # g is assigned the same reference as f
h = [1, 2, 3]  # h is a new list with the same content
print(f is g)  # this will check if f and g refer to the same object, which is True
#output: True
print(f is h)  # this will check if f and h refer to the same object, which is False
#output: False
print(f == h)  # this will check if f and h have the same content, which is True
#output: True