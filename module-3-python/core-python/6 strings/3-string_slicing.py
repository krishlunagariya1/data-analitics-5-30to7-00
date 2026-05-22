name = "Krish"

print(name[0:3])
#output: kri
print(name[1:3])
#output: ri
print(name[1:-1]) # is same as name[1:4]
#output: rish
print(name[:3]) # is same as name[0:3]
#output: kri
print(name[1:]) # is same as name[1:5]
#output: rish
print(name[-4:]) # is same as name[1:5]
#output: rish
print(name[::2]) # this will print every second character of the string, starting from index 0
#output: kih
print(name[1::2]) # this will print every second character of the string, starting from index 1
#output: ris
print(name[::-1]) # this will print the string in reverse order
#output: hsirK

print(name[0:5:2]) # this will print every second character of the string, starting from index 0 and ending at index 4
#output: kih
print(name[1:5:2]) # this will print every second character of the string, starting from index 1 and ending at index 4
#output: ris
print(name[2:4:4]) # this will print every second character of the string, starting from index 2 and ending at index 4
#output: i


