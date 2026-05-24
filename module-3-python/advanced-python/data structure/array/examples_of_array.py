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


# emp=["brijesh","kumar","het"]
# print(emp)
# print(emp[1])
# print(type(emp))

# import array as arr
# i=[45,25,36,39,41]
# res=arr.array('i',i)
# print(res)


# import array as arr
# i=[45,25,36,39,41]
# res=arr.array('i',i)
# print(type(res))

# res=arr.array('i',i)
# print(type(res[0]))
# print((res[0]))


# add at end of array or list
# marks=[45,36,85,79]
# marks.append(43)
# print(marks)


# removed data 
# marks=[45,36,85,79]
# marks.pop()
# print(marks)

# update a data from array 

# marks=[45,36,85,79]
# marks[1]=100
# print(marks)

# slicing 

# marks=[45,36,85,79]
# # print(marks[:0])
# # print(marks[::-1])
# print(marks[1::])



# array 

#data=[2,4,6,3,5]
# print(data*2)

# data=[2,4,5,8,10]
# for i in data:
#     print(i*2)


# data=[2,4,5,8,10]
# for i in data:
#     print(i**2)


# data=[2,4,5,8,10]
# for i in data:
#     print(i**3)




# price=[200,500,400,300,50]
# profit=max(price) - min(price)
# print("Profits is :",profit)

# cart managements 
cart=[300,400,499,599]
total=sum(cart)
print("Total of cart :",total)
# provides discount
disscount=0.2 * total
print("Total discount :",disscount)

profit=total - disscount
print("Total of profit :",profit)