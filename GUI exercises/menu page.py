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
image = Image.open('toggle2 icon.png').resize((30, 30))
toggle_icon = ImageTk.PhotoImage(image)
menu_bar = Frame(root, bg='#384B70')
toggle_button = Button(menu_bar, image=toggle_icon, bg='#384B70')
toggle_button.place(x=4, y=10)
menu_bar.pack(side=LEFT, fill=Y, padx=3, pady=4)
menu_bar.pack_propagate(flag=False)

menu_bar.configure(width=45)

root.mainloop()

