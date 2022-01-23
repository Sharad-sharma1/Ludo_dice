import random
from tkinter import *
from tkinter.messagebox import showinfo

root=Tk()
root.geometry("700x250")

l1 = Label(root,font=("times",100))

def roll():
    number = ['\u2680', '\u2681','\u2682','\u2683','\u2684', '\u2685']
    j = random.choice(number)
    l1.config(text=f'{j}')
    l1.pack()
    if j == '\u2685':
        lb = showinfo("Chance","Hurray!!!!! You got another chance to roll")

b1 = Button(root,text="Click to roll the dice",command=roll)
b1.place(x=295,y=0)




root.mainloop()
