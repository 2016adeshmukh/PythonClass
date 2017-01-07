from decimal import *
r=2.9
oldx = .25
news = 0
for i in range(400):
    newx = r * oldx * (1 - oldx)
    print newx
    oldx=newx
