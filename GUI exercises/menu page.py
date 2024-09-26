import tkinter as tk 
from tkinter import messagebox as msg
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry('600x600')
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

def indicator(indi_lbl, page_switch):

    home_ind.config(bg='#5271ff')
    info_ind.config(bg='#5271ff')
    method_ind.config(bg='#5271ff')
    account_ind.config(bg='#5271ff')

    indi_lbl.config(bg='white')
    if menu_bar.winfo_width() > 45:
        fold_menu()

    for frame in page.winfo_children():
        frame.destroy()
    page_switch()

image6 = Image.open('close.png').resize((30, 30))
close_icon = ImageTk.PhotoImage(image6)

image7 = Image.open('Wallpaper2.png').resize((500, 600))
wallp = ImageTk.PhotoImage(image7)

def animate_menu():
    current_width = menu_bar.winfo_width()
    if not current_width > 200:
        current_width += 10
        menu_bar.config(width=current_width)

        root.after(ms=8, func=animate_menu)

def extend_menu():
    animate_menu()
    toggle_button.config(image=close_icon)
    toggle_button.config(command=fold_menu)

def animate_folding():
    current_width = menu_bar.winfo_width()
    if current_width != 45:
        current_width -= 10
        menu_bar.config(width=current_width)

        root.after(ms=8, func=animate_folding)

def fold_menu():

    animate_folding()
    toggle_button.config(image=toggle_icon)
    toggle_button.config(command=extend_menu)

def home():
    h_page=Frame(page)
    lb = Label(h_page, image=image7)
    lb.place()

    h_page.pack(fill=BOTH, expand=True)

def methods():
    #label
    m_page=Frame(page)
    lb = Label(m_page, text='SELECT MODELS', font=('Times new Roman', 20, 'bold'))
    lb.place(x=150, y=200)
    #combobox
    entry = StringVar()
    methods  = ttk.Combobox(m_page, width=15, textvariable=entry)
    methods['values']=('RF-GWO model','RF-TPE model','HGB-GWO model','HGB-TPE model')
    methods.place(x=200, y=250)
    #button
    btn = Button(m_page, text='Confirm')
    btn.place(x=230, y=290)

    m_page.pack(fill=BOTH, expand=True)

def info():
    i_page=Frame(page)
    lb = Label(i_page, text='This is a Rock Fragmentation App \nMade by Central South University foreign student', font=('Times new Roman', 12,))
    lb.place(x=100, y=200)

    i_page.pack(fill=BOTH, expand=True)


page = Frame(root, bg='#D8D2C2')
page.place(relheight=1.0, relwidth=1.0, x=50)
#home()
#methods()
info()

#widgets/buttons
menu_bar = Frame(root, bg='#5271ff')
toggle_button = Button(menu_bar, image=toggle_icon, bg='#5271ff', bd=0, 
                       activebackground='#5271ff', command=extend_menu)
toggle_button.place(x=4, y=10)

#home icon
home_button = Button(menu_bar, image=home_icon, bg='#5271ff', 
                     bd=0, activebackground='#5271ff', command=lambda: indicator(indi_lbl=home_ind, page_switch=home))
home_button.place(x=6, y=100, height=40, width=30) 

home_ind = Label(menu_bar, bg='white')
home_ind.place(x=3, y=100, height=40, width=3)

home_label = Label(menu_bar, text='Home', bg='#5271ff', fg='white',
                   font=('Arial', 15), anchor=W)
home_label.place(x=45, y=100, width=100, height=40)
home_label.bind('<Button-1>', lambda e: indicator(indi_lbl=home_ind, page_switch=home ))

#methods icon
methods_button = Button(menu_bar, image=methods_icon, bg='#5271ff', 
                        bd=0, activebackground='#5271ff', command=lambda: indicator(indi_lbl=method_ind, page_switch=methods))
methods_button.place(x=6, y=170, height=40, width=30)

method_ind = Label(menu_bar, bg='#5271ff')
method_ind.place(x=3, y=170, height=40, width=3)

method_label = Label(menu_bar, text='Models', bg='#5271ff', fg='white',
                   font=('Arial', 15), anchor=W)
method_label.place(x=45, y=170, width=120, height=40)
method_label.bind('<Button-1>', lambda e: indicator(indi_lbl=method_ind, page_switch=methods))

#info_icon
info_button = Button(menu_bar, image=info_icon, bg='#5271ff', 
                     bd=0, activebackground='#5271ff', command=lambda: indicator(indi_lbl=info_ind, page_switch=info))
info_button.place(x=6, y=240, height=40, width=30)

info_ind = Label(menu_bar, bg='#5271ff')
info_ind.place(x=3, y=240, height=40, width=3)

info_label = Label(menu_bar, text='Info', bg='#5271ff', fg='white',
                   font=('Arial', 15), anchor=W)
info_label.place(x=45, y=240, width=100, height=40)
info_label.bind('<Button-1>', lambda e: indicator(indi_lbl=info_ind, page_switch=info))

#account_icon
account_button = Button(menu_bar, image=account_icon, bg='#5271ff', bd=0, 
                        activebackground='#5271ff', command=lambda: indicator(indi_lbl=account_ind))
account_button.place(x=6, y=310, height=40, width=30)

account_ind = Label(menu_bar, bg='#5271ff')
account_ind.place(x=3, y=310, height=40, width=3)

account_label = Label(menu_bar, text='Account', bg='#5271ff', fg='white',
                   font=('Arial', 15), anchor=W)
account_label.place(x=45, y=310, width=120, height=40)
account_label.bind('<Button-1>', lambda e: indicator(indi_lbl=account_ind))

menu_bar.pack(side=LEFT, fill=Y, padx=3, pady=4)
menu_bar.pack_propagate(flag=False)

menu_bar.configure(width=45)

root.mainloop()

