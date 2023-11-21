from tkinter import *
import tkinter
from tkinter.tix import COLUMN
window = Tk()
window.geometry("800x600")
window.title("may tinh phuong trinh bac 2")

#text
lbl1 = Label(window,text = "nhập a",fg="black",font=("Arial" , 20))
lbl1.grid(column=0,row=0)

lbl2 = Label(window,text = "nhập b",fg="black",font=("Arial" , 20))
lbl2.grid(column=1,row=0)

lbl3 = Label(window,text = "nhập c",fg="black",font=("Arial" , 20))
lbl3.grid(column=2,row=0)

#textbox
txt1 = Entry(window,width=20)
txt1.grid(column = 0,row=1)

txt2 = Entry(window,width=20)
txt2.grid(column = 1,row=1)

txt3 = Entry(window,width=20)
txt3.grid(column = 2,row=1)


#ans
ans1 = Label(window,text =" ",fg="black",font=("Arial,",20))
ans2 = Label(window,text ="" ,fg="black",font=("Arial,",20))
ans1.grid(column=1,row=3)
ans2.grid(column=1,row=4)

def HandleButton():

    a = int(txt1.get())
    b = int(txt2.get())
    c = int(txt3.get())
    denta=b*b-4*a*c
    if a!=0:
        if denta >= 0:
            k1=(-b+denta**(1/2))/(2*a)
            k2=(-b-denta**(1/2))/(2*a)
            
        else:
            k1=complex((-b/(2*a)),((-denta)**(1/2))/(2*a))
            k2=complex((-b/(2*a)),(-(-denta)**(1/2))/(2*a))
        
        x1 = list(str(k1))
        x2 = list(str(k2))
        x1[len(x1) - 2] = 'i'
        x2[len(x2) - 2] = 'i'
        ans1.configure(text = ('x1=',x1))
        ans2.configure(text = ('x2=',x2))

    else:
        if(b==0)and(c!=0):
            ans1.configure(text = "vô nghiệm")
        if(b==0)and(c==0):
            ans1.configure(text ="pt co tap nghiem R")
        if(b!=0):
            ans1.configure(text = ('x=',b/c))
    
    return


#button
btn = Button(window,text = "giải phương trình" , fg="black" ,font=("Arial",30),command=HandleButton)
btn.grid(column=1,row=2)
window.mainloop()   