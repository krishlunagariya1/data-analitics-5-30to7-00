a = {1, 2, 4}
b = {3, 4, 5}

print(a.union(b))  # Output: {1, 2, 3, 4, 5}
print(a.intersection(b))  # Output: {4}
print(a.difference(b))  # Output: {1, 2}
print(a.symmetric_difference(b))  # Output: {1, 2, 3, 5}
