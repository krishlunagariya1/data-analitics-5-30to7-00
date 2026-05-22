# list is a collection of items in a particular order. 
# It is mutable, 
# meaning you can change its content without changing its identity.
#  Lists are defined by enclosing elements in square brackets [] and separating them with commas.

names = ["krish", "patel", "jayesh", "shubham"]
elements = [1, 34, 67, False, True]

print(names) 
print(type(names))
print(elements[0])
print(elements[1]) 

print(elements[1:4]) # Output: [34, 67, False]

# List Methods
print(len(elements)) # Output: 5

# list in python is mutable
elements[2] = 69
print(elements) # Output: [1, 34, 69, False, True]