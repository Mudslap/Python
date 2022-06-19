##Basic Format
##from tkinter import *
##root = Tk()
##label = Label(root, text = "I am a label widget")
##button = Button(root, text = "I am a button widget",command=exit)
##
##label.pack()
##button.pack()
##
##root.mainloop()

##Display text and buttons project
from tkinter import *
root=Tk()
root.geometry(("300x200"))
root.resizable(width=False, height=False)

color="gray"

v=IntVar()
def calculate():
    g=entry.get()
    val=v.get()
    money=int(g)*val
    print("$"+str(money))
    entry2.insert(END,money)
    
label = Label(root, text = "Please select an item")
label.place(x=100, y=5)

radio1 = Radiobutton(root , text = "Milk"  , bg = color , variable = v,value=5 )
radio1.place(x=100,y=20)
radio2 = Radiobutton(root , text = "Chocolate Cake"  , bg = color,variable = v,value=20  )
radio2.place(x=100,y=40)
radio3 = Radiobutton(root , text = "Peach"  , bg = color ,variable = v,value=9 )
radio3.place(x=100,y=60)

label2 = Label(root, text = "Quantity:")
label2.place(x=20, y=80)
button= Button(root, text = "Cal:",command=calculate)
button.place(x=30, y=100)
entry=Entry(root, width=25)
entry2=Entry(root, width=25)
entry.place(x=80,y=80)
entry2.place(x=80,y=100)

root.mainloop

##Inputs/Quiz
##from tkinter import *
##import time
##root = Tk()
##entry = Entry(root)
##def correct():
##    r=Label(root, text = "Correct!!")
##    r.pack()
##    root.update()
##    time.sleep(1)
##    exit()
##def wrong():
##    b=Label(root, text = "U Wrong!!")
##    b.pack()
##    root.update()
##    time.sleep(1)
##    exit()
##label = Label(root, text = "Hi")
##label2 = Label(root, text = "I'm Fat")
##label3 = Label(root, text = "Pop Quiz!! What's my name")
##
##button3 = Button(root, text = "A) Fat",command=wrong)
##button1 = Button(root, text = "B) Vincent",command=correct)
##button2 = Button(root, text = "C) Hi I'm Fat",command=wrong)
##
##label.pack()
##label2.pack()
##label3.pack()
##button3.pack()
##button1.pack()
##button2.pack()
##
##
##root.mainloop()

##Images
##from tkinter import *
##root = Tk()
##jr=PhotoImage(file="/home/pi/jr.png")
##l=Label(root,image=jr)
##w=PhotoImage(file="/home/pi/warriors.png")
##w=Label(root,image=w)
##jr=PhotoImage(file="/home/pi/jr.png")
##l=Label(root,image=jr)
##jr=PhotoImage(file="/home/pi/jr.png")
##l=Label(root,image=jr)
##jr=PhotoImage(file="/home/pi/jr.png")
##l=Label(root,image=jr)
##jr=PhotoImage(file="/home/pi/jr.png")
##l=Label(root,image=jr)
##l.pack()
##w.pack()
##root.update()
##root.mainloop()

##Quiz App
##from tkinter import *
##bob= Tk()
##bob.geometry(("300x125"))
##def printtext():
##    g1=entry.get()
##    g2=entry2.get()
##    print(g1,g2)
##
##def clear():
##    entry.delete(0,END)
##    entry2.delete(0,END)
##I1=Label(bob,text="Enter First Name").grid(row=0)
##entry =Entry(bob)
##entry.grid(row=0,column=1)
##I2=Label(bob,text="Enter Last Name").grid(row=2)
##entry2 =Entry(bob)
##entry2.grid(row=2,column=1)
##button = Button(bob, text = "press to print out name",command=printtext)
##button.grid(row=3,column=0)
##button2 = Button(bob, text = "clear the text",command=clear)
##button2.grid(row=4,column=0)
##button3 = Button(bob, text = "exit the game",command=exit)
##button3.grid(row=5,column=0)

##Password
##from tkinter import *
##import random
##import time
##bob=Tk()
##username="ViolinsAreCoolAid"
##password="PeepleRBald"
##counter=0
##
##def guess():
##    global counter
##    guessu=e.get()
##    guessp=e2.get()
##    if username!=guessu or guessp!=password:
##        print("access denied")
##        I2=Label(bob,text="Access Denied")
##        I2.grid(row=3,column=1)
##        counter=counter+1
##        if counter==3:
##            I2=Label(bob,text="3 tries are over. Activating Nuclear Bombs...")
##            I2.grid(row=3,column=1)
##            bob.update()
##            time.sleep(2)
##            exit()
##    if username==guessu and guessp==password:
##        print("access granted")
##        I2=Label(bob,text="Access Granted")
##        I2.grid(row=3,column=1)
##        bob.update()
##        time.sleep(2)
##        exit()
##I1=Label(bob,text="Username")
##I1.grid(row=0)
##e=Entry(bob)
##e.grid(row=0,column=1)
##
##I2=Label(bob,text="Password")
##I2.grid(row=2)
##e2=Entry(bob,show='*')
##e2.grid(row=2,column=1)
##
##button=Button(bob,text="Log In",command=guess)
##button.grid(row=3)
##mainloop()

##Number guessing
##from tkinter import *
##import random
##import time
##bob=Tk()
##number=random.randint(1,100)
##def guess():
##    g=entry.get()
##    g=int(g)
##    if g==number:
##        c=Label(bob,text="correct")
##        c.pack()
##        bob.update()
##        time.sleep(2)
##        exit()
##    if number>g:
##        h=Label(bob,text="higher")
##        h.pack()
##    if number<g:
##        l=Label(bob,text="lower")
##        l.pack()
##I1=Label(bob,text="Guess a number from 1-100")
##I1.pack()
##entry=Entry(bob)
##entry.pack()
##
##button=Button(bob,text="guess number",command=guess)
##button.pack()

##celcius to fahrenheit
##from tkinter import *
##bob=Tk()
##def ctofcalculate():
##    c=entry.get()
##    c=int(c)
##    f=c*9/5+32
##    entry2.insert(0,f)
##def ftoccalculate():
##    f=entry2.get()
##    f=int(f)
##    c=(f-32)*5/9
##    entry.insert(0,c)
##def clear():
##    entry.delete(0,END)
##    entry2.delete(0,END)
##I1=Label(bob,text="Celcius").grid(row=0)
##entry=Entry(bob)
##entry.grid(row=0,column=1)
##
##I1=Label(bob,text="Fahrenheit").grid(row=2)
##entry2=Entry(bob)
##entry2.grid(row=2,column=1)
##
##button=Button(bob,text="celcius to fahrenheit",command=ctofcalculate)
##button.grid(row=3)
##
##button3=Button(bob,text="fahrenheit to celcius",command=ftoccalculate)
##button3.grid(row=4)
##
##button2 = Button(bob, text = "clear the text",command=clear)
##button2.grid(row=5,column=0)
##mainloop()


