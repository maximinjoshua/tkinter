from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Image Viewer')

image_1=ImageTk.PhotoImage(Image.open('D:/tkinter/pictures_for_img_viewer/shaun.jpg'))
image_2=ImageTk.PhotoImage(Image.open('D:/tkinter/pictures_for_img_viewer/shaun1.jpg'))
image_3=ImageTk.PhotoImage(Image.open('D:/tkinter/pictures_for_img_viewer/shaun2.jpg'))
imglist=[image_1,image_2,image_3]

label=Label(root, image=image_1)
label.grid(row=0, column=0, columnspan=3)



def fwd_click(imgnumber):
    global label
    global fwdbutton
    global backbutton
    
    label.grid_forget()
    label=Label(root, image=imglist[imgnumber])
    label.grid(row=0, column=0, columnspan=3)
    fwdbutton=Button(root, text='>>', command=lambda:fwd_click(imgnumber+1))
    if imgnumber==2:
        fwdbutton=Button(root, text='>>', state=DISABLED)
    fwdbutton.grid(row=1, column=2)
    backbutton=Button(root, text='<<', command=lambda:back_click(imgnumber-1))
    backbutton.grid(row=1, column=0)


    
    
def back_click(imgnumber):
    global label
    global fwdbutton
    global backbutton
    label.grid_forget()
    label=Label(root, image=imglist[imgnumber])
    label.grid(row=0, column=0, columnspan=3)
    fwdbutton=Button(root, text='>>', command=lambda:fwd_click(imgnumber+1))
    fwdbutton.grid(row=1, column=2)
    backbutton=Button(root, text='<<', command=lambda:back_click(imgnumber-1))
    if imgnumber==0:
        backbutton=Button(root, text='<<', state=DISABLED)
    backbutton.grid(row=1, column=0)

fwdbutton=Button(root, text='>>', command=lambda:fwd_click(1))
backbutton=Button(root, text='<<', command=back_click, state=DISABLED)
fwdbutton.grid(row=1, column=2)
backbutton.grid(row=1, column=0)
    
    



root.mainloop()
