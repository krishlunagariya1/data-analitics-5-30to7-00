student = {
     "name": "Krish",
     "city": "Delhi",
     "company": "meta",
        "age": 23,
}

print(student["company"])
# print(student["hobby"]) #give an error because there is no key named "hobby" in the dictionary

print(student.get("hobby")) # this will return None because there is no key named "hobby" in the dictionary

student["city"] = "gaziabad" # this will update the value of the key "city" to "gaziabad"
print(student) 

