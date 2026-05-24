import array as arr
emp=[45,36,25,78,96]
res=arr.array("i",emp)
print(res)

# find sum of array
res=arr.array("i",emp)
print(sum(res))
#output: 280
print(max(res))
#output: 96
print(min(res))
#output: 25
print((res))
#output: array('i', [45, 36, 25, 78, 96])