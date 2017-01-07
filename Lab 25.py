from Tkinter import *
from random import *

root=Tk()
canvas=Canvas(root, width=600, height=600, bg='white')
canvas.pack()
def makeCloud(evnt): # Method that writes all words based on times they appear
    canvas.delete(ALL)
    colors={0:'red',1:'black',2:'yellow',3:'red',4:'green',5:'blue'}
    aaa=0
    while aaa<len(final):
        bbb=randint(0,5)
        canvas.create_text(randint(100,500),randint(100,500), fill=colors[bbb],text=final[aaa], font=("Arial",finalb[aaa]))
        aaa+=1

declaration=open('declaration.txt').read().split() 
common=open('common.txt').read().split(',') # opens and splits both files

a=0 # defines variables
b=0
c=0
d=0
e=0
tempcount=0
countlen=0
counter=[]
declength=0
declength=len(declaration)# finds lengths of text files
comlength=len(common)

while a<declength: # while loop 
    if ',' in declaration[a]:
        declaration[a]=declaration[a].replace(",","") # removes ,
        a+=1
    elif '-' in declaration[a]:
        declaration[a]=declaration[a].replace("-","") # removes -
        a+=1
    elif ':' in declaration[a]:
        declaration[a]=declaration[a].replace(":","") # removes :
        a+=1
    elif '.' in declaration[a]:
        declaration[a]=declaration[a].replace(".","") # removes .
        a+=1
    elif ';' in declaration[a]:
        declaration[a]=declaration[a].replace(";","") # removes ;
        a+=1
    elif '&' in declaration[a]:
        declaration[a]=declaration[a].replace("&","") # removes &
        a+=1
    else:
        a+=1
a=0
while a<declength: # Takes away all common words from list
    while b<comlength:
        if declaration[a].upper()==common[b].upper():
            declaration.remove(declaration[a])
            declength=len(declaration)
            a-=1
            b=comlength
        else:
            declaration[a]=declaration[a].lower() # makes all words lowercase
            b+=1
    b=0
    a+=1
while c<declength: #Counts how many times word appears in array
    counter.append(declaration[c])
    counter.append(declaration.count(declaration[c]))
    c+=1
countlen=len(counter)
a=0
b=0
c=0
ax=[]
bx=[]
while a<countlen: # Takes all words that appear more than 5 times
    if a%2==1:
        if counter[a]>=5:
            ax.append(counter[a-1])
            bx.append(counter[a])
            a+=1
        else:
            a+=1
    else:
        a+=1
a=0
final=[]
finalb=[]# appends words appearing more than 5 times to final array
while len(ax)!=0:
    a=ax[1]
    final.append(a) # saves word once
    finalb.append(bx[1]*5) # saves size once and scales it
    b=0
    while b<len(ax): # deletes all other appearances of that word
        if ax[b]==a:
            ax.remove(a)
            bx.remove(bx[b]) # deletes times they appear
            b=b
        else:
            b+=1
root.bind('<space>',makeCloud)
root.mainloop()

