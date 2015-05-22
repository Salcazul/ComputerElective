subject1 = raw_input("What is your first subject?")
grade1 = raw_input("What is your grade in this subject?")

subject2 = raw_input("What is your second subject?")
grade2 = raw_input("What is your grade in this subject?")

subject3 = raw_input("What is your third subject?")
grade3 = raw_input("What is your grade in this subject?")

subject4 = raw_input("What is your fourth subject?")
grade4 = raw_input("What is your grade in this subject?")

gpa1 = 0
gpa2 = 0
gpa3 = 0
gpa4 = 0

if grade1 == "A":
    gpa1 = 4.00
elif grade1 == "B":
    gpa1 = 3.00
elif grade1 == "C":
    gpa1 = 2.00
elif grade1 == "D":
    gpa1 = 1.00
elif grade1 == "F":
    gpa1 = 0.00

if grade2 == "A":
    gpa2 = 4.00
elif grade2 == "B":
    gpa2 = 3.00
elif grade2 == "C":
    gpa2 = 2.00
elif grade2 == "D":
    gpa2 = 1.00
elif grade2 == "F":
    gpa2 = 0.00
    
if grade3 == "A":
    gpa3 = 4.00
elif grade3 == "B":
    gpa3 = 3.00
elif grade3 == "C":
    gpa3 = 2.00
elif grade3 == "D":
    gpa3 = 1.00
elif grade3 == "F":
    gpa3 = 0.00
    
if grade4 == "A":
    gpa4 = 4.00
elif grade4 == "B":
    gpa4 = 3.00
elif grade4 == "C":
    gpa4 = 2.00
elif grade4 == "D":
    gpa4 = 1.00
elif grade4 == "F":
    gpa4 = 0.00

gpa = ((gpa1 + gpa2 + gpa3 + gpa4) / 4)

print "Your GPA is:", gpa
