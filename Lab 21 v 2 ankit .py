from decimal import *
r=2.9
x = .25
a=0
b=0
c=0
for i in range(400):
    a=(r*(x**2))
    b= (r*x)
    c=b-a
    x=c
    print i+1, x
