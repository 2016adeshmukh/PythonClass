from decimal import * # imports decimal
x=3.7 # sets x0 to 3.7
a=0 # a is 0
b=0 # b is 0
for c in range (20): # for loop that goes 20 times
    a=Decimal(4)-Decimal(x) # sets a to 4-x
    b=Decimal(1)/Decimal(a) # sets b to 1/a so 1/4-x
    x=Decimal(b) # x is b
    print c+1, x # prints trial and x

