x=0.25 # sets x to 0.25
r=3.99 # sets r to 2.9
a=0 # sets a to 0
b=0 # sets b to 0
for j in range (400): # for loop in range 400
    if j<99: # checks if j is lesss than 100 trials
        print "Skip" # skips first 10 trials
    else: # if j is greater than 100 trails
        a=(1-x) # a = 1-x
        b=(r*x) # b = r*x
        x=(a*b) # x = r*x*(1-x)
        print x # prints new x
