# #5) ''    a grad evaluation of student if marks >= 90 print A
# 						>= 75 tack user from input B
# 						>= 50 tack user from input C
# 						    tack user from unput fail

marks = float(input("Enter the marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


    