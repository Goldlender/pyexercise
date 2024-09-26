import tkinter as tk 
from tkinter import messagebox as msg
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry('400x600')
root.title('Menu')
#root.withdraw()

#icons 
image = Image.open('toggle.png').resize((30, 30))
toggle_icon = ImageTk.PhotoImage(image)

image2 = Image.open('home.png').resize((30, 30))
home_icon = ImageTk.PhotoImage(image2)

image3 = Image.open('methods.png').resize((30, 30))
methods_icon = ImageTk.PhotoImage(image3)

image4 = Image.open('info.png').resize((30, 30))
info_icon = ImageTk.PhotoImage(image4)

image5 = Image.open('account.png').resize((30, 30))
account_icon = ImageTk.PhotoImage(image5)

#widgets/buttons
menu_bar = Frame(root, bg='#5271ff')
toggle_button = Button(menu_bar, image=toggle_icon, bg='#5271ff', bd=0, activebackground='#5271ff')
toggle_button.place(x=4, y=10)

home_button = Button(menu_bar, image=home_icon, bg='#5271ff', bd=0, activebackground='#5271ff')
home_button.place(x=6, y=100) 

methods_button = Button(menu_bar, image=methods_icon, bg='#5271ff', bd=0, activebackground='#5271ff')
methods_button.place(x=6, y=150)

info_button = Button(menu_bar, image=info_icon, bg='#5271ff', bd=0, activebackground='#5271ff')
info_button.place(x=6, y=200)

account_button = Button(menu_bar, image=account_icon, bg='#5271ff', bd=0, activebackground='#5271ff')
account_button.place(x=6, y=250)

menu_bar.pack(side=LEFT, fill=Y, padx=3, pady=4)
menu_bar.pack_propagate(flag=False)

menu_bar.configure(width=45)

root.mainloop()

