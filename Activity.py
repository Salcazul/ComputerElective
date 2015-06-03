#   1. Create a program that allows the user to enter three numbers
#   and the program should recognize which is the highest number.

n1 = input("Enter a number.")
n2 = input("Enter a second number.")
n3 = input("Enter a third number.")

n4 = 0

if n1 > n2 and n1 > n3:
    n4 = n1
elif n2 > n1 and n2 > n3:
    n4 = n2
else:
    n4 = n3

print "The highest number is", n4
