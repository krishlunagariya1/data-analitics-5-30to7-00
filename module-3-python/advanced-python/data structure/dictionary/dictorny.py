emp = dict({"name": "John", "age": 30, "city": "New York"})
print(emp.get("name"))  
print(emp.get("age"))
print(emp.get("city"))
#output: John
#30
#New York

# nested dictionary
fruits = {1:"banana", 2:"apple", 3:{"a":"avocado", "b":"grape", "c":"orange"}}
print(fruits)
print(fruits[3])
print(fruits[3]["a"])
#output: {1: 'banana', 2: 'apple', 3: {'a': 'avocado', 'b': 'grape', 'c': 'orange'}}
#avocado

# dictionary add items
emp = {1:"krish", 2:"raj", 3:"suresh"}
emp[4] = "ramesh"
emp.update({5:"suresh"})
print(emp)
#output: {1: 'krish', 2: 'raj', 3: 'suresh', 4: 'ramesh', 5: 'suresh'}

#delete dictionary
emp = {1:"krish", 2:"raj", 3:"suresh"}
del emp[2]
print(emp)
#output: {1: 'krish', 3: 'suresh'}



