list=[1,2,2,2,3,4,5,6,78,6,5,4,4,43,33,2,2,2,2,2,55]
print list.count(3)
ankit=[3,3,3,2,2,4,5,6,754,2,1]
a=ankit[1]
b=0
while b<len(ankit):
    if ankit[b]==a:        
        ankit.remove(a)
        b=b
    else:
        b+=1
print ankit
