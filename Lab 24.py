from Tkinter import *
#from random import *
def makeCloud(evnt): # Method that writes all State Names based on Size
    canvas.delete(ALL)
    colors={0:'red',1:'black',2:'yellow',3:'red',4:'green',5:'blue'}
    for aaa in range (51):
        bbb=randint(0,5)
        canvas.create_text(randint(100,500),randint(100,500), fill=colors[bbb],text=fullName[aaa], font=("Arial",font[aaa]))

root=Tk() # Makes a window
canvas=Canvas(root, width=600, height=600, bg='white')
canvas.pack()

reada=[] # creates an array
readb=[]
popSize=[]
NamePopA=[]
NamePopB=[]
fullName=[]
font=[]
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
        font.append(15) # merges data from both arrays
        c+=1 # increments c
    elif popSize[c]<=2688418:
        print fullName[c], "Font Size: 18"
        font.append(18)
        c+=1
    elif popSize[c]<=4468976:
        print fullName[c], "Font Size: 21"
        font.append(21)
        c+=1
    elif popSize[c]<=7078515:
        print fullName[c], "Font Size: 24"
        font.append(24)
        c+=1
    else:
        print fullName[c], "Font Size: 27"
        font.append(27)
        c+=1

canvas.bind("<space>", makeCloud) # Binds spacebar to makeCloud
root.mainloop()
    

