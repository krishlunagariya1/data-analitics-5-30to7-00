# w.a.p to add elements of one list to another list using extend() method
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list1.extend(list2)
print("After extending list1 with list2:", list1)
#output: After extending list1 with list2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# w.a.p to find the largest number in a list
numbers = [10, 20, 30, 5, 15, 25, 35]
largest = max(numbers)
print("The largest number in the list is:", largest)
#output: 35

# w.a.p to find the smallest number in a list
smallest = min(numbers)
print("The smallest number in the list is:", smallest)
#output: 5

# w.a.p to find the sum of all numbers in a list
total_sum = sum(numbers)
print("The sum of all numbers in the list is:", total_sum)
#output: 140

# w.a.p to find the average of all numbers in a list
average = total_sum / len(numbers)
print("The average of all numbers in the list is:", average)
#output: 20.0

# w.a.p to find the length of a list
length = len(numbers)
print("The lenth of the list is:", length)
#output: 7

# w.a.p to find the number of occurrences of a specific element in a list
my_list = [1, 2, 3, 4, 5, 2, 2]
element = 2
occurrences = my_list.count(element)
print(f"The number of occurrences of {element} in the list is: {occurrences}")
#output: 3

# w.a.p to find the index of the first occurrence of a specific element in a list
index = my_list.index(element)
