def greet(name="User", city="Delhi"):
    print("Hello", name, city)

greet() # Output: Hello User Delhi
greet("Krish") # Output: Hello Krish Delhi
greet(city="Rajkot", name="Krish") # Output: Hello Krish Rajkot


# labda function
add = lambda a, b: a + b
print(add(4, 6)) # Output: 10