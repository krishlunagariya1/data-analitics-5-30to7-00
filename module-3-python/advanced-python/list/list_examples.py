# defind list of numbers

numbers = [1, 2, 3, 4, 5]
# print the list of numbers
print(numbers)

# define a list of strings
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

# define a list of mixed data types
mixed_list = [1, "hello", 3.14, True, None]
print(mixed_list)

# define a list of lists
list_of_lists = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(list_of_lists)

# how to repeat list 

# define a list of numbers
numbers = [1, 2, 3]
# repeat the list 3 times
repeated_numbers = numbers * 3
print(repeated_numbers)

# insert in list : insert an exlement at a specific position in the list
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)

#extend list : add all the elements of another list to the end of the current list
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
numbers.extend(more_numbers)
print(numbers)
#output: [1, 2, 3, 4, 5, 6]

#insert list : insert an element at a specific position in the list
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)
#output: ['apple', 'orange', 'banana', 'cherry']

employees = ["krish", "jayesh", "patel", "shah"]
employees.insert(2, "john")
print(employees)
#output: ['krish', 'jayesh', 'john', 'patel', 'shah']

#remove() method : remove the first occurrence of a specified value from the list
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)
#output: [1, 2, 4, 5]

#remove all data from list : clear() method is used to remove all items from a list, leaving it empty
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)
#output: []
# add data in list : append() method is used to add an item to the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
#output: [1, 2, 3, 4]

#remove all data using remove() method :
my_list = [1, 2, 3, 4, 5]
for i in my_list[:]:  # Iterate over a copy of the list
    my_list.remove(i)
print(my_list)
#output: []

my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)
    my_list.remove(i)
print(my_list)
#output: 1

#update list : update an element at a specific index in the list
my_list = [10 , 20 , 30 , 40 , 50]
my_list[0] = 100
print(my_list)
#output: [100, 20, 30, 40, 50]

my_list[2] = 70
print(my_list)
#output: [100, 20, 70, 40, 50]

#pop() method : remove and return an item at a given index (default is the last item)
my_list = [1, 2, 3, 4, 5]   
popped_item = my_list.pop(2)  # Remove the item at index 2 (value 3)
print(popped_item)  # Output: 3
print(my_list)  # Output: [1, 2, 4, 5]

#sort() method : sort the items of the list in ascending order
my_list = [5, 2, 9, 1, 5, 6]
my_list.sort()
print(my_list)
#output: [1, 2, 5, 5, 6, 9]

#desending order sort : sort the items of the list in descending order
my_list = [5, 2, 9, 1, 5, 6]
my_list.sort(reverse=True)
print(my_list)
#output: [9, 6, 5, 5, 2, 1]

