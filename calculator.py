from tkinter import *
root=Tk()

def button_click(number):
    current=entry_cal.get()
    entry_cal.delete(0,END)
    entry_cal.insert(0,str(current)+str(number))

def add():
    global f_num
    global condition
    condition='addition'
    f_num=entry_cal.get()
    entry_cal.delete(0,END)

def sub():
    global f_num
    global condition
    condition='subtraction'
    f_num=entry_cal.get()
    entry_cal.delete(0,END)

def mul():
    global f_num
    global condition
    condition='multiplication'
    f_num=entry_cal.get()
    entry_cal.delete(0,END)

def div():
    global f_num
    global condition
    condition='division'
    f_num=entry_cal.get()
    entry_cal.delete(0,END)

def equal():
    second_number=entry_cal.get()
    entry_cal.delete(0,END)
    if(condition=='addition'):
        entry_cal.insert(0, int(f_num)+int(second_number))
    elif(condition=='subtraction'):
        entry_cal.insert(0, int(f_num)-int(second_number))
    elif(condition=='multiplication'):
        entry_cal.insert(0, int(f_num)*int(second_number))
    elif(condition=='division'):
        entry_cal.insert(0, int(f_num)/int(second_number))
         

def clear():
    entry_cal.delete(0,END)
    
entry_cal=Entry(root)
button1=Button(root,text='1', padx=40,bg='red', command=lambda: button_click(1))
button2=Button(root,text='2', padx=40,bg='green', command=lambda: button_click(2))
button3=Button(root,text='3', padx=40,bg='pink', command=lambda: button_click(3))
button4=Button(root,text='4', padx=40,bg='gold', command=lambda: button_click(4))
button5=Button(root,text='5', padx=40,bg='silver', command=lambda: button_click(5))
button6=Button(root,text='6', padx=40,bg='violet', command=lambda: button_click(6))
button7=Button(root,text='7', padx=40,bg='purple', command=lambda: button_click(7))
button8=Button(root,text='8', padx=40,bg='yellow', command=lambda: button_click(8))
button9=Button(root,text='9', padx=40,bg='blue', command=lambda: button_click(9))
button0=Button(root,text='0', padx=40,bg='orange', command=lambda: button_click(0))
button_add=Button(root,text='+', padx=40, command=add)
button_equal=Button(root,text='=', padx=87, command=equal)
button_mul=Button(root,text='x', padx=40, command=mul)
button_div=Button(root,text='/', padx=41, command=div)
button_clear=Button(root,text='clear', padx=79, command=clear)
button_sub=Button(root,text='-', padx=40, command=sub)



entry_cal.grid(row=0, column=0, columnspan=3)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_sub.grid(row=4, column=2)
button_mul.grid(row=5, column=0)
button_div.grid(row=6, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_equal.grid(row=6, column=1, columnspan=2)

root.mainloop()
