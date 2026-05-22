a = {1, 2, 4}
b = {3, 4, 5}

print(a.union(b)) #union of two sets will give us a new set that contains all the unique elements from both sets.
 # Output: {1, 2, 3, 4, 5}
print(a.intersection(b)) #intersection of two sets will give us a new set that contains only the elements that are present in both sets.
 # Output: {4}
print(a.difference(b)) #difference of two sets will give us a new set that contains only the elements that are in the first set but not in the second set.
 # Output: {1, 2}
print(a.symmetric_difference(b)) #symmetric difference of two sets will give us a new set that contains only the elements that are in either set but not in both.
 # Output: {1, 2, 3, 5}
print(a.issubset(b)) #issubset method will tell us if all elements of the first set are present in the second set.
 # Output: False
print(a.issuperset(b)) #issuperset checks first set contains all elements of the second set.
 # Output: False

