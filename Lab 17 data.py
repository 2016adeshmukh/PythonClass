from random import *
from math import *

xp=[]
yp=[]
dist=[]
counter=0
avg=0
td=0
standev=0
range1=3000
range2=1000

a=0
for a in range (1000):
    xp.append(300)
    yp.append(300)

b=0
c=0
d=0
for b in range (range1):
    for c in range (range2):
        d=randint(0,3)
        if d==0:
            xp[c]+=1
            d=sqrt(((xp[c]-300)**2)+((yp[c]-300)**2))
            td+=d
            dist.append(d)
        elif d==1:
            xp[c]-=1
            d=sqrt(((xp[c]-300)**2)+((yp[c]-300)**2))
            td+=d
            dist.append(d)
        elif d==2:
            yp[c]+=1
            d=sqrt(((xp[c]-300)**2)+((yp[c]-300)**2))
            td+=d
            dist.append(d)
        else:
            yp[c]-=1
            d=sqrt(((xp[c]-300)**2)+((yp[c]-300)**2))
            td+=d
            dist.append(d)
avg=td/(range1*range2)
for aaa in range(len(dist)):
    counter+=((dist[aaa]-avg)**2)
standev=sqrt(counter/(range1*range2))
for bbb in range((range1*range2)):
    if bbb<=1000:
        fd=(1/(standev*(sqrt(2*pi))))*(e**((-1*(bbb-avg)**2)/(2*(standev**2))))
        print bbb, fd
