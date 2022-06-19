from tkinter import *
root=Tk()
root.title(("Calculator"))
##root.geometry(("180x150"))
#root.resizable(width = False , height = False)
def seven():
    entry1.insert(END,'7')
def eight():
    entry1.insert(END,'8')
def nine():
    entry1.insert(END,'9')
def divide():
    entry1.insert(END,'/')
def four():
    entry1.insert(END,'4')
def five():
    entry1.insert(END,'5')
def six():
    entry1.insert(END,'6')
def multiply():
    entry1.insert(END,'*')
def one():
    entry1.insert(END,'1')
def two():
    entry1.insert(END,'2')
def three():
    entry1.insert(END,'3')
def minus():
    entry1.insert(END,'-')
def zero():
    entry1.insert(END,'0')
def period():
    entry1.insert(END,'.')
def equal():
    g= entry1.get()
    g=eval(g)
    entry1.delete(0,END)
    entry1.insert(END,g)
     
    
def add():
    entry1.insert(END,'+')
def delete():
    entry1.delete(0,END)
    

entry1=Entry(root,)
entry1.grid(row=0,column=0,columnspan=4)


##Row1
button7 = Button(root, text = "7",command=seven)
button7.grid(row=2,column=0,sticky=W)
button8 = Button(root, text = "8",command=eight)
button8.grid(row=2,column=1,sticky=W)
button9 = Button(root, text = "9",command=nine)
button9.grid(row=2,column=2,sticky=W)
buttondiv = Button(root, text = "/",command=divide)
buttondiv.grid(row=2,column=3,sticky=W)


##Row2
button4= Button(root, text = "4",command=four)
button4.grid(row=3,column=0,sticky=W)
button5 = Button(root, text = "5",command=five)
button5.grid(row=3,column=1,sticky=W)
button6= Button(root, text = "6",command=six)
button6.grid(row=3,column=2,sticky=W)
buttonx = Button(root, text = "x",command=multiply)
buttonx.grid(row=3,column=3,sticky=W)

##Row3
button1= Button(root, text = "1",command=one)
button1.grid(row=4,column=0,sticky=W)
button2 = Button(root, text = "2",command=two)
button2.grid(row=4,column=1,sticky=W)
button3= Button(root, text = "3",command=three)
button3.grid(row=4,column=2,sticky=W)
buttonmin = Button(root, text = "-",command=minus)
buttonmin.grid(row=4,column=3,sticky=W)


##Row4
button0= Button(root, text = "0",command=zero)
button0.grid(row=5,column=0,sticky=W)
button = Button(root, text = ".",command=period)
button.grid(row=5,column=1,sticky=W)
buttonequ= Button(root, text = "=",command=equal)
buttonequ.grid(row=5,column=2,sticky=W)
buttonadd = Button(root, text = "+",command=add)
buttonadd.grid(row=5,column=3,sticky=W)

##Row5
button0= Button(root, text = "Clear",command=delete)
button0.grid(row=6,column=0,columnspan=4)

root.mainloop()
