xarr=[]
yarr=[]
x1=[]
y1=[]

x=0.25
r=2.9 # 3.21, 3.5, 2.9, 3.99
a=0 
b=0 
c=0
d=0
j=0
y=0
while j<1:
    a=j**2
    b=r*a
    c=r*j
    d=c-b
    y=d
    print j, y
    j+=0.01
