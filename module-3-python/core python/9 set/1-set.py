'''
s1 = {1, 5, 6, 9, 12, 1, 5}
s2 = () # empty set

print(s1)  # Output: {1, 5, 6, 9, 12}
print(type(s1))  # Output: <class 'set'>
'''

items = {"apple", "banana", "tomato"}

items.add("orange")  # Adding an item to the set
print(items)  # Output: {'apple', 'banana', 'orange'}

items.update(["mango", "peach"]) # Adding multiple items to the set
print(items)  # Output: {'apple', 'banana', 'orange', 'mango', 'peach'}


items.remove("banana")  # Removing an item from the set
print(items)  # Output: {'apple', 'orange', 'mango', 'peach'}

items.discard("grape")  # Discarding an item that may not exist (no error)
print(items)  # Output: {'apple', 'orange', 'mango', 'peach'}

items.pop()  # Removing an arbitrary item from the set
print(items)  # Output: {'orange', 'mango', 'peach'} (one item removed)

items.clear()  # Removing all items from the set
print(items)  # Output: set() (empty set)

print(len(items))  # Output: 0 (length of the set)