from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
#from random import *
import random
from captcha.image import ImageCaptcha
import string
from io import BytesIO


P=tk.Tk()
P.title("CAPTCHA")
P.config(background= '#CD5C5C')



#background image

"""img2=PhotoImage(file= "BACK.png")
canvas= Canvas(P,width=400,height= 400)
canvas.pack(expand=True, fill= BOTH)

#Add the image in the canvas
canvas.create_image(0,0,image=img2, anchor="center")"""





#captcha instance
image=ImageCaptcha(width=200,height=150)
#captcha object
captcha_text=str(random.randint(100000,999999))
data=image.generate(captcha_text)
#save the captcha
image.write(captcha_text,"CAPCHA.png")

#font type
font1=font.Font(family="Helvetica",weight="bold",size=20,slant="italic")
font2=font.Font(family="Cooper Black",size=30)
font3=font.Font(family="Times New Roman",weight="bold",size=25)


#label
label2=Label(P,width=35,height=2,bg="#DEB887",fg="black",relief="solid",borderwidth=6,text="MY CAPTCHA GENERATOR")
label2["font"]=font2
label2.place(x=300,y=50)

user=0
#func for captcha
def accept():
    global user
    user=txt1.get(1.0,"end-1c")
    if (captcha_text==user):
        messagebox.showinfo("P","accepted")
        txt1.delete("1.0","end")
        P.destroy()
    else:
        #user=txt1.get(1.0,"end-1c")
        messagebox.showerror("P","enter valid captcha")
        txt1.delete("1.0","end")
        change_captcha()
#button for submit
button1=Button(P,command=accept,width=10,height=2,bg="#ECF0F1",fg="#A0522D",relief="raised",borderwidth=10,text="SUBMIT",font=font1)
button1.place(x=250,y=600)

#func for changing
def change_captcha():
    global captcha_text
    #captcha instance
    image=ImageCaptcha(width=200,height=150)
    #captcha object
    captcha_text=str(random.randint(100000,999999))
    data=image.generate(captcha_text)
    #save the captcha
    image.write(captcha_text,"CAPCHA.png")
    img2=PhotoImage(file="CAPCHA.png")
    button3.config(image=img2)
    button3.update()
    UpdateButton()

#button for reset
button2=Button(P,command=change_captcha,width=10,height=2,bg="#ECF0F1",fg="#A0522D",relief="raised",borderwidth=10,text="RESET",font=font1)
button2.place(x=1000,y=600)

#text for enter captcha
txt1=Text(P,width=25,height=3,bg="#ffffff",fg="#f53163",relief="groove",borderwidth=14)
txt1["font"]=font3
txt1.place(x=900,y=300)


#button for captcha
img1=PhotoImage(file="CAPCHA.png")
button3=Button(P,width=500,height=100,bg="#DAA520",fg="#800000",relief="sunken",borderwidth=7,image=img1,font=font1,text="MERA CAPTCHA:   ",compound="right")
button3.place(x=210,y=300)



P.geometry("1920x1080")
P.state('zoomed')
P.mainloop()

