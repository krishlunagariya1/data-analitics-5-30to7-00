age = 16

if age >= 18:
    print("You can drive!")
else:
    print("You cannot drive!")
# Output: You cannot drive!

score = 75
if score >= 80:
    print("Grade A")
elif score >= 60:
    print("Greade B")
else:
    print("Grade C")
# Output: Grade B

if score % 2 == 0:
    print("Score is even")
else:
    print("Score is odd")
# Output: Score is odd

#ternary operator
age = 20
status = "Adult" if age>= 18 else "Minor"
print(status)
# Output: Adult

#pass statement
age = 16

if age > 20:
   pass
else:
    print("Else code")
# Output: Else code