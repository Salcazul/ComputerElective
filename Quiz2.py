#Name
name = raw_input("What is your name?")

#Last Name
last = raw_input("What is your last name?")

#Class
classname = raw_input("What class are you in?")

#Year of birth
year = input("What is your year of birth?")

#Calculate current age
age = 2015 - year
print "You are", age, "years of age."
#Computer grade 1S
s1 = input("What is your first semester grade?")

#Computer grade 2S
s2 = input("What is your second semester grade?")

#Calculate final grade
final = (s1 + s2) / 2

#Print in a string name, lastname, class, final grade
print "Your name is", name, last+". Your final grade in", classname, "is", final, "."
