# Examples of Array in Python

# 1. Creating an Array
# Using the array module
import array
# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)

# 2. Accessing Elements
print(arr[0])  # Output: 1
print(arr[2])  # Output: 3

# 3. Modifying Elements
arr[1] = 10
print(arr)  # Output: array('i', [1, 10, 3, 4, 5])

# 4. Appending Elements
arr.append(6)
print(arr)  # Output: array('i', [1, 10, 3, 4, 5, 6])

# 5. Removing Elements
arr.remove(10)
print(arr)  # Output: array('i', [1, 3, 4, 5, 6])

# 6. Length of the Array
print(len(arr))  # Output: 5

# 7. Iterating through the Array
for element in arr:
    print(element)
# Output: 1
#         3
#         4
#         5
#         6


