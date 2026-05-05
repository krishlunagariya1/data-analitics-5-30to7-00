items = ["apple", "banana", "cherry"]

print(len(items))  # Output: 3

items.append("orange")  # Adding an item to the list
print(items)  # Output: ['apple', 'banana', 'cherry', 'orange']

items.insert(1, "grape")  # Inserting an item at a specific index
print(items)  # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']

items.extend(["more banans", "pineapple"])  # Extending the list with another list
print(items)  # Output: ['apple', 'grape', 'banana', 'cherry', 'orange', 'more banans', 'pineapple']

items.remove("banana")  # Removing an item from the list
print(items)  # Output: ['apple', 'grape', 'cherry', 'orange', 'more banans', 'pineapple']

items.pop()  # Removing the last item from the list
print(items)  # Output: ['apple', 'grape', 'cherry', 'orange', 'more banans']

items.reverse()  # Reversing the list
print(items)  # Output: ['more banans', 'orange', 'cherry', 'grape', 'apple']   

items.sort()  # Sorting the list
print(items)  # Output: ['apple', 'cherry', 'grape', 'more banans', 'orange']

items.index("banana")  # This will raise an error since "banana" has been removed from the list 

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Sorting the list of numbers
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]

print(11 in numbers)  # Output: False
print(5 in numbers)   # Output: True

