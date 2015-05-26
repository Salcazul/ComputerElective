'''
Show the value of a number in Dollars, Euros, Yens
Ask the user to input a number
Ask to input the currency
Show the exchange
'''

value = input("What is your amount?")
currency = raw_input("What is your currency?")

if currency == "dollars":
    print "Your value in euros is:", value * 1.09
    print "Your value in yens is:", value * 0.0081
elif currency == "euros":
    print "Your value in dollars is:", value * 0.92
    print "Your value in yens is:", value * 0.0074
else:
    print "Your value in dollars is:", value * 123.09
    print "Your value in euros is:", value * 134.39
