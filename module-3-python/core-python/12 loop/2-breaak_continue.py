from matplotlib.pylab import iterable


for i in range(1, 10):
    if i == 5:
        break # Exit the loop when i is 5
    print(i) # Output: 1 2 3 4

for i in range(1, 10):
    if i == 5:
        continue # Skip the rest of the loop when i is 5
    print(i) # Output: 1 2 3 4 6 7 8 9


