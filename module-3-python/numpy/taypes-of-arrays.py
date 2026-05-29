import numpy as np

# 0-dimensional or scalar array
scalar = np.array(5)
print(scalar)  # Output: 5
print("Type of scalar:", type(scalar))  
# Output: <class 'numpy.ndarray'>


# 1-dimensional array
vector = np.array([1, 2, 3, 4, 5])
print(vector)  # Output: [1 2 3 4 5]
print("Type of vector:", type(vector))  
# Output: <class 'numpy.ndarray'>

# 2-dimensional array
import numpy as np
matrix = np.array([[1, 2], [3, 4]])
print(matrix)  # Output: [[1 2]
              #          [3 4]]
print("Type of matrix:", type(matrix))  
# Output: <class 'numpy.ndarray'>

# n-dimensional array
import numpy as np
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor) # Output: [[[1 2]
              #          [3 4]]
              #         [[5 6]
              #          [7 8]]]


