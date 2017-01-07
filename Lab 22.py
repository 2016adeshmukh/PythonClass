from Tkinter import * # import Tkinter

root=Tk()
canvas=Canvas(root, width=300, height=300, bg='white') # Makes a window
canvas.pack()

r=2 # defines all variables
x0=0.25
x1=0
a=0
b=0
c=0
d=0
e=0
while r<4:# starts r at 2 and goes until r is 4
    d=(r-2)*150 # scales r
    for c in range(9100): # goes 9100 times
        a=(r*x0) 
        b=(1-x0)
        x0=(a*b) # sets x0 at (r*x0*(1-x0))
        e=(x0*299) # scales x0
        if c>9000: # plots the last 100 trials
            canvas.create_rectangle(d,e,d,e,fill='black')
    c=0 # resets variables
    x0=0.25
    r+=0.01 # increments r


root.mainloop() # ends program
