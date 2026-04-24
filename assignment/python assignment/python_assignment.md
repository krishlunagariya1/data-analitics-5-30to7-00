# Python Assignment

## 1) What are the types of Applications?

Applications can be classified by how they are used, deployed, or built. Common types include:

- **Desktop Applications**: Installed on a personal computer (e.g., text editors, spreadsheets).
- **Web Applications**: Run in a browser and are hosted on a web server (e.g., online stores, email services).
- **Mobile Applications**: Designed for smartphones and tablets (e.g., social apps, navigation apps).
- **Console Applications**: Run in a command-line interface or terminal.
- **Client-Server Applications**: Use a client to request services from a server over a network.
- **Embedded Applications**: Run on dedicated hardware devices (e.g., smart appliances, IoT devices).

## 2) What is programming?

Programming is the process of writing instructions that a computer can execute. These instructions are written in a programming language to solve problems, perform operations, or automate tasks.

## 3) What is Python?

Python is a high-level, interpreted programming language known for its readability and ease of use. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

## 4) Python program to check if a number is positive, negative or zero

```python
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

### Sample Output

```
Enter a number: 5
The number is positive.
```

## 5) Python program to get the factorial of a given number

```python
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Factorial of {n} is {factorial}.")
```

### Sample Output

```
Enter a non-negative integer: 5
Factorial of 5 is 120.
```

## 6) Python program to get the Fibonacci series of a given range

```python
n = int(input("Enter the number of Fibonacci terms: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()
```

### Sample Output

```
Enter the number of Fibonacci terms: 7
0 1 1 2 3 5 8 
```

## 7) How memory is managed in Python?

Python memory management includes:

- **Automatic memory allocation**: Python allocates memory for objects automatically.
- **Garbage collection**: Python frees memory for objects that are no longer referenced.
- **Reference counting**: Each object tracks how many references point to it.
- **Memory pools**: The interpreter uses memory pools to reduce fragmentation and speed allocation.

## 8) What is the purpose of the `continue` statement in Python?

The `continue` statement skips the rest of the current loop iteration and moves to the next iteration. It is used when you want to ignore part of a loop body for certain conditions.

## 9) Python program that swaps two numbers with and without a temporary variable

### With a temporary variable

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swap: a = {a}, b = {b}")

temp = a
a = b
b = temp

print(f"After swap with temp: a = {a}, b = {b}")
```

### Sample Output

```
Enter first number: 3
Enter second number: 8
Before swap: a = 3, b = 8
After swap with temp: a = 8, b = 3
```

### Without a temporary variable

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swap: a = {a}, b = {b}")

a, b = b, a

print(f"After swap without temp: a = {a}, b = {b}")
```

### Sample Output

```
Enter first number: 3
Enter second number: 8
Before swap: a = 3, b = 8
After swap without temp: a = 8, b = 3
```

## 10) Python program to find whether a given number is even or odd

```python
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

### Sample Output

```
Enter an integer: 4
The number is even.
```

## 11) Python program to test whether a passed letter is a vowel or not

```python
letter = input("Enter a letter: ").lower()
if letter in "aeiou" and len(letter) == 1:
    print("The letter is a vowel.")
else:
    print("The letter is not a vowel.")
```

### Sample Output

```
Enter a letter: a
The letter is a vowel.
```

## 12) Python program to sum three given integers, but result is zero if two values are equal

```python
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

if a == b or b == c or a == c:
    print("0")
else:
    print(a + b + c)
```

### Sample Output

```
Enter first integer: 2
Enter second integer: 3
Enter third integer: 4
9
```

## 13) Python program that returns true if two integers are equal or their sum or difference is 5

```python
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))

result = (x == y) or (x + y == 5) or (abs(x - y) == 5)
print(result)
```

### Sample Output

```
Enter first integer: 2
Enter second integer: 3
True
```

## 14) Python program to sum the first n positive integers

```python
n = int(input("Enter a positive integer: "))
if n > 0:
    total = n * (n + 1) // 2
    print(f"Sum of the first {n} positive integers is {total}.")
else:
    print("Please enter a positive integer.")
```

### Sample Output

```
Enter a positive integer: 5
Sum of the first 5 positive integers is 15.
```

## 15) Python program to calculate the length of a string

```python
text = input("Enter a string: ")
print(f"The length of the string is {len(text)}.")
```

### Sample Output

```
Enter a string: hello
The length of the string is 5.
```

## 16) Python program to count the number of characters (character frequency) in a string

```python
text = input("Enter a string: ")
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequencies:")
for char, count in frequency.items():
    print(f"{repr(char)}: {count}")
```

### Sample Output

```
Enter a string: hello
Character frequencies:
'h': 1
'e': 1
'l': 2
'o': 1
```

## 17) What are negative indexes and why are they used?

Negative indexes allow access to elements from the end of a sequence in Python. For example, `-1` gives the last item, `-2` gives the second last item, and so on. They are used for convenient access to the tail of lists, strings, and other sequences without needing to compute the length.

## 18) Python program to count occurrences of a substring in a string

```python
text = input("Enter the text: ")
substring = input("Enter the substring: ")
count = text.count(substring)
print(f"The substring '{substring}' appears {count} times.")
```

### Sample Output

```
Enter the text: banana bandana
Enter the substring: ana
The substring 'ana' appears 2 times.
```
