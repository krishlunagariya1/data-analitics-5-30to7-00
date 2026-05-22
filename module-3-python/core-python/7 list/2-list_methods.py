import numbers


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

#items.index("banana")  # This will raise an error since "banana" has been removed from the list 

num = [1, 3, 6, 5]

print(max(num))  # Output: 6
print(min(num))  # Output: 1

num.append(10)
print(num)  # Output: [1, 3, 6, 5, 10]

num.insert(2, 4)
print(num)  # Output: [1, 3, 4, 6, 5, 10]

num.sort()
print(num)  # Output: [1, 3, 4, 5, 6, 10]

num.reverse()
print(num)  # Output: [10, 6, 5, 4, 3, 1]

num.pop() # Removing the last item from the list
print(num)  # Output: [10, 6, 5, 4, 3]

num.remove(4) # Removing the item with value 4 from the list
print(num)  # Output: [10, 6, 5, 3]

num.clear() # Removing all items from the list
print(num)  # Output: [] (empty list)

num.append(1) # Adding an item to the list
print(num)  # Output: [1]

num.count(1) # Counting the occurrences of the value 1 in the list
print(num.count(1))  # Output: 1

num.count(2) # Counting the occurrences of the value 2 in the list
print(num.count(2))  # Output: 0

num.count(3) # Counting the occurrences of the value 3 in the list
print(num.count(3))  # Output: 0







