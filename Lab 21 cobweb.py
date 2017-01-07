x0=0.25
x1=0
increment=0
r=3.5
a=0
b=0
c=0
for increment in range (400):
    a=x0**2
    b=r*a
    c=r*x0
    x1=c-b
    if increment>100:
        print x0,x1
        print x1, x1
    x0=x1


