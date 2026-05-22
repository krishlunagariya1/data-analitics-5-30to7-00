text = "python"

print(text)
#output: python
print(len(text))  # this will print the length of the string
#output: 6
print(text.upper())  # this will print the string in uppercase letters
#output: PYTHON
print(text.lower())  # this will print the string in lowercase letters
#output: python
print(text.capitalize())  # this will print the string with the first letter capitalized and the rest in lowercase
#output: Python
print(text.replace("p", "k"))  # this will replace the letter "p" with the letter "k" in the string
#output: kython
print(text.find("n"))  # this will print the index of the first occurrence of the letter "n" in the string
#output: 5
print(text.count("p"))  # this will print the number of times the letter "p" appears in the string
#output: 1
print(text.startswith("p"))  # this will print True if the string starts with the letter "p", otherwise it will print False
#output: True
print(text.endswith("n"))  # this will print True if the string ends with the letter "n", otherwise it will print False
#output: True

print(text.replace("python","Java"))
#output: Java