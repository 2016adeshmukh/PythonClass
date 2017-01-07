reada=[] # creates an array
readb=[]
popSize=[]
NamePopA=[]
NamePopB=[]
fullName=[]
merge=[]
reada=open('lab314.txt').read().split() # reads and splits text file
readb=open('lab411.txt').read().split('\n') # reads and splits text file
a=0
while a <len(reada): # while loop as long as length of reada
    if a%2!=0: # if number is odd
        reada[a]=int(reada[a]) #convert to int
        popSize.append(reada[a]) # append it to popSize
        a+=1
    else: # if number is even
        NamePopA.append(reada[a]) # append it to numpopa
        a+=1
b=0
while b<len(readb): #while loop as long as length of readb
    if b%2!=0: # if number is odd
        fullName.append(readb[b]) # append it to fullname
        b+=1
    else: # if number is even
        NamePopB.append(readb[b]) # append it to numpopb
        b+=1
c=0
while c<len(popSize): # while loop as long as length of pop size
    if popSize[c]<=1211537: # checks to see how large # is 
        print fullName[c], "Font Size: 15" # prints state name and font size
        merge.append((fullName[c], popSize[c])) # merges data from both arrays
        c+=1 # increments c
    elif popSize[c]<=2688418:
        print fullName[c], "Font Size: 18"
        merge.append((fullName[c], popSize[c]))
        c+=1
    elif popSize[c]<=4468976:
        print fullName[c], "Font Size: 21"
        merge.append((fullName[c], popSize[c]))
        c+=1
    elif popSize[c]<=7078515:
        print fullName[c], "Font Size: 24"
        merge.append((fullName[c], popSize[c]))
        c+=1
    else:
        print fullName[c], "Font Size: 27"
        merge.append((fullName[c], popSize[c]))
        c+=1
