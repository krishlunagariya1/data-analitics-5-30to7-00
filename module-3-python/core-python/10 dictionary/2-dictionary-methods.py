student = {
     "name": "Krish",
     "city": "Delhi",
     "company": "meta",
        "age": 23,
}

student.pop("name") # this will remove the key "name" and its value from the dictionary
print(student)
#output: {'city': 'Delhi', 'company': 'meta', 'age': 23}

student["class"] = "12th" # this will add a new key "class" with the value "12th" to the dictionary
print(student)
#output: {'city': 'Delhi', 'company': 'meta', 'age': 23, 'class': '12th'}

student.popitem() # this will remove the last key-value pair from the dictionary
print(student)
#output: {'city': 'Delhi', 'company': 'meta', 'age': 23}

del student["city"] # this will remove the key "city" and its value from the dictionary
print(student)
 #output: {'company': 'meta', 'age': 23, 'class': '12th'}

print(student.keys()) # this will return a list of all the keys in the dictionary
#output: dict_keys(['company', 'age', 'class'])

print(student.values()) # this will return a list of all the values in the dictionary
#output: dict_values(['meta', 23, '12th'])

print(student.items()) # this will return a list of all the key-value pairs in the dictionary as tuples
#output: dict_items([('company', 'meta'), ('age', 23), ('class', '12th')])
print(student)