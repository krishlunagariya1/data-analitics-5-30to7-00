#tuple is a collection of ordered and immutable elements.
#  It is defined using parentheses () and can contain elements of different data types.

numbers = (1, 2, 3, 4, 5)  # This is a tuple
print(numbers)
print(type(numbers))

# Tuples are immutable, so we cannot change their elements
# numbers[0] = 10  # This will raise an error
# However, we can create a new tuple by concatenating existing tuples
new_numbers = numbers + (6, 7)
print(new_numbers)  # Output: (1, 2, 3, 4, 5, 6, 7)
# We can also use tuple unpacking to assign values to variables
a, b, c, d, e = numbers
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4
print(e)  # Output: 5

# singale element tuple
single_element_tuple = (42,)  # Note the comma
print(single_element_tuple)  # Output: (42,)
print(type(single_element_tuple))  # Output: <class 'tuple'>
 