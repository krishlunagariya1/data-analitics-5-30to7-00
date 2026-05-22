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

# 8. Using NumPy for Arrays
import numpy as np
np_arr = np.array([1, 2, 3, 4, 5])
print(np_arr)
print(type(np_arr))  # Output: <class 'numpy.ndarray'>

# 9. Multi-dimensional Arrays with NumPy
np_2d_arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np_2d_arr)
print(type(np_2d_arr))  # Output: <class 'numpy.ndarray'>
