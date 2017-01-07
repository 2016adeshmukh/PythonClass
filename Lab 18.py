x=[] # makes array x
y=[] # makes array y
score=[] # makes array score
total=0 # sets total to 0
z=0 # sets z to 0
for a in range(10): # for loop that goes 10 times
    print a+1 # prints trial number
    d=int(raw_input('Enter number: ')) # asks user for input
    x.append(d) # sets input in x array
    if  a==9: # if it is bowl 10
        d=int(raw_input('Enter number: ')) # takes input from user
        y.append(d) # sets input to y array
        if x[a]==10: # if it was a strike
            z=int(raw_input('Enter number: ')) # sets z to another input
        elif y[d]+x[d]==10: # if it was a spare
            z=int(raw_input('Enter number: ')) # sets z to another input
        else: # if it was a regular bowl
            z=0 # z =0
            
    else: # if it is not the last bowl
        if d==10: # if it was a strike
            y.append(0) # then there is no second bowl
        else: # if it is not a strike
            d=int(raw_input('Enter number: ')) # takes input from user
            y.append(d) # adds input to array y
print x # prints array x
print y # prints array y
print z # prints z
total=0 # sets total to 0


for b in range(10): # for loop that goes 10 times
    if b==9: # if it is the last bowl
        total+=(x[b]+y[b]+z) # total is the sum of last x, last y, and z
        score.append(total) # appends total to score
    elif b==8: # else if it is bowl 9
        if x[b]==10: # if it is a strike
            total+=(x[b]+x[b+1]+y[b+1]) # total is addition of 10 + next x, next y
            score.append(total) # appends total to score
        elif x[b]+y[b]==10: # if it is a spare
            total+=(10+x[b+1]) # total is 10 + next bowl
            score.append(total) # appends total to score
        else: # if it is a regular bowl
            total+=(x[b]+y[b]) # total is sum of x and y
            score.append(total) # appends total to score
    else: # if it is not bowl 9 or bowl 10
        if x[b]==10: # if it is a strike
            if x[b+1]==10:# if next bowl is a strike
                total+=(x[b]+x[b+1]+x[b+2])# total is 10+10+next bowl
                score.append(total) # appends total to score
            else: # if next bowl is not a strike
                total+=(x[b]+x[b+1]+y[b+1])# total is addition of 10 + next x, next y
                score.append(total) # appends total to score
        elif x[b]+y[b]==10: # if it is a spare
            total+=(10+x[b+1])# total is 10 + next bowl
            score.append(total)# appends total to score
        else: # if it is a regular bowl
            total+=(x[b]+y[b]) # total is sum of x and y
            score.append(total) # appends total to score
            
print score # prints array score
print "Your final score is: ", score[9] # prints final score
