from tkinter import *
from tkinter import messagebox
import PIL.Image
from PIL import ImageTk



from recognize import *

##from test_model import *
def detectingv():
    messagebox.showinfo("Info","Detection from live Video Started")
    detect()


#print("guiiiiiiiiiiiiiiii")
top =Tk()
top.title("Sign language Prediction")
top.configure(background='white')
fp = open("sky.jpg","rb")
img_ar = PIL.Image.open(fp)
ph_ar = ImageTk.PhotoImage(img_ar)
lbl_ar = Label(top,image=ph_ar)
lbl_ar.image = ph_ar

btn_bis=Button(top,text="Start",height="0",width="15",command=lambda:detectingv())
lbl_ar.grid(row=2,columnspan=5)

btn_bis.place(x=300,y=30)

top.mainloop()


