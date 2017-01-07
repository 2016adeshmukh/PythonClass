from decimal import * # imports decimal
x=5 # sets x to 5
b=0 # sets b to 0
c=0 # sets c to 0
d=0 # sets d to 0
for a in range (5): # for loop that goes 5 times
    b=Decimal(2)/Decimal(x) # finds 2/x
    c=Decimal(x)+Decimal(b) # adds x to 2/x
    d=Decimal(c)/(2) # divides x + 2/x by 2
    x=Decimal(d) # x now equals 0.5(x+2/x)
    print a+1, x # prints out trial and value of x
