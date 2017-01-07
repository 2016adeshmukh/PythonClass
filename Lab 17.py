# imports neccessary items
from Tkinter import *
from random import *
from math import *

#Makes all variables and arrays
xp=[]
yp=[]
dist=[]
counter=0
avg=0
td=0
standev=0
range1=100
range2=1000

#Makes a window and packs it
root=Tk()
canvas=Canvas(root, width=600, height=600, bg='white')
canvas.pack()

#Creates 1000 rectangles at 300,300
a=0
for a in range (1000):
    canvas.create_rectangle(300,300,300,300, fill='black')

#Appends 300 to xp and yp 100 times to show where rectangles are
b=0
for b in range (1000):
    xp.append(300)
    yp.append(300)

c=0
d=0
f=0
for c in range (range1):
    canvas.delete(ALL)
    for d in range (range2):
        f=randint(0,3)
        if f==0:
            xp[d]+=1 # Moves one to the right
            canvas.create_rectangle(xp[d],yp[d],xp[d],yp[d], fill='black') # moves rectangle
            d=sqrt(((xp[c]-300)**2)+((yp[c]-300)**2)) #calculates distance
            td+=d # keeps running total
            dist.append(d) # saves distance of point from center
        elif f==1:
            xp[d]-=1 # Moves one to the left
            canvas.create_rectangle(xp[d],yp[d],xp[d],yp[d], fill='black')
            d=sqrt(((xp[c]-300)**2)+((yp[c]-300)**2))
            td+=d
            dist.append(d)
        elif f==2:
            yp[d]+=1# Moves one up
            canvas.create_rectangle(xp[d],yp[d],xp[d],yp[d], fill='black')
            d=sqrt(((xp[c]-300)**2)+((yp[c]-300)**2))
            td+=d
            dist.append(d)
        else:
            yp[d]-=1 # Moves one down
            canvas.create_rectangle(xp[d],yp[d],xp[d],yp[d], fill='black')
            d=sqrt(((xp[c]-300)**2)+((yp[c]-300)**2))
            td+=d
            dist.append(d)
avg=td/(range1*range2) # calculates average
for aaa in range(len(dist)): # finds the total sum of (distance-average) squared
    counter+=((dist[aaa]-avg)**2)
standev=sqrt(counter/(range1*range2)) # calculates standard deviation
for bbb in range((range1*range2)): 
    if bbb<=1000:
        fd=(1/(standev*(sqrt(2*pi))))*(e**((-1*(bbb-avg)**2)/(2*(standev**2)))) # Finds probability
        print bbb, fd # Prints points
root.mainloop() # Ends window
