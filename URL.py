from tkinter import *
import pyshorteners
from PIL import Image, ImageTk
import cv2

a=Tk()
a.geometry('400x420')
a.configure(background="light pink")
a.title("URL SHORTNER")
heading= Label(a,text="URL SHORTNER",fg="black",bg="pink",font=("Times",25,'bold'))
heading.pack(side=TOP)

url = StringVar()
url_short = StringVar()

Label(a, text='Enter URL here', bg='pink', fg='black', font='Times 10 bold').place(x=50, y=100)
Entry(a, textvariable=url, width=35, font='Times 12').place(x=50, y=120)

Label(a, text='URl Shortener here', bg='pink', fg='black',
      font='Times 10 bold').place(x=50, y=200)
text = Entry(a, width=47, textvariable=url_short)
text.place(x=50, y=220)


def Convert_fun():
    con_url = pyshorteners.Shortener().tinyurl.short(url.get())
    url_short.set(con_url)


Button(a, text='Convert', bg='#fff', fg='#000', font='Times 15 bold', command=Convert_fun).place(x=150, y=150)

a.mainloop()

