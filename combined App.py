import tkinter as tk 
from tkinter import messagebox as msg
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


root = Tk()
root.title('Sign In')
root.geometry('400x400')
root.configure(bg='#B7B7B7')

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

image6 = Image.open('close.png').resize((30, 30))
close_icon = ImageTk.PhotoImage(image6)

image7 = Image.open('Wallpaper2.png').resize((590, 590))
wallp = ImageTk.PhotoImage(image7)


class Sign_in:
        def __init__(self, master):
                self.myframe = Frame(master, bg='#B7B7B7')
        
                def login():
                        username = 'Admin'
                        password = '12345'
                        if username_e.get()==username and password_e.get()==password:
                                msg.showinfo(title='Login Successful', message='You logged in Successfully')
                                #root.withdraw()
                                MethodWindow()
                        else:
                                msg.showerror(title='Login Failed', message='Invalid username or password')
                                close()

                def MethodWindow():
                        top = Toplevel()
                        top.geometry('200x200')
                        frame = Frame(top)
                        #frame.configure(height=200, width=300)
                        
                        top.title('Select Method')
                        label = Label(top, text = 'Select Model',font=('Times new roman',16, 'bold'))
                        label.pack(pady=20)


                        options = ['RF-TPE model',
                           'RF-GWO model',
                           'HGB-GWO model',
                           'HGB-TPE model'
                           ]
                        
                        combo = ttk.Combobox(top,values=options)
                        combo.pack(pady=10)

                        button = Button(top, text = 'Confirm')
                        button.pack(pady=20)

                        frame.pack(padx=10, pady=10)


                

                login_l = Label(self.myframe, text='LOGIN', bg='#B7B7B7', fg='#16325B', font=('Courier New',25, 'bold'))
                username_l = Label(self.myframe, text='Username', bg='#B7B7B7', fg='#181C14', font=('Times New Roman',14, 'bold'))
                username_e = Entry(self.myframe, font=('Courier New',12))
                password_e = Entry(self.myframe, show='*', font=('Courier',12))
                password_l = Label(self.myframe, text='Password', bg='#B7B7B7', fg='#181C14', font=('Times New Roman',14, 'bold'))
                login_b = Button(self.myframe, text='Login', bg='#16325B', fg='#FCF8F3', font=('Times New Roman',14, 'bold'), command = login)

                #placing widgets
                login_l.grid(row=0, column=0, columnspan=2, sticky='news', pady=30)
                username_l.grid(row=1, column=0)
                username_e.grid(row=1, column=1, pady=15)
                password_l.grid(row=2, column=0)
                password_e.grid(row=2, column=1, pady=15)
                login_b.grid(row=3, column=0, columnspan=2, pady=30)

                def close(self):
                        MethodWindow()
                        #root.quit()
                        #root.destroy()
                        exit()

                # def login(self):
                #         self.username = 'Admin'
                #         self.password = '12345'
                #         if username_e.get()==self.username and password_e.get()==self.password:
                #                 msg.showinfo(title='Login Successful', message='You logged in Successfully')
                #                 #root.withdraw()
                #                 MethodWindow()
                #         else:
                #                 msg.showerror(title='Login Failed', message='Invalid username or password')
                #                 close()

                self.myframe.pack()


class Menu:
     def __init__(self, master):
          self.master = root
          self.master.geometry('600x600')
          self.master.title('Menu')

               #widgets/buttons
          menu_bar = Frame(root, bg='#5271ff')
          toggle_button = Button(menu_bar, image=toggle_icon, bg='#5271ff', bd=0, 
                                activebackground='#5271ff', command=self.extend_menu)
          toggle_button.place(x=4, y=10)

            #home icon
          home_button = Button(menu_bar, image=home_icon, bg='#5271ff', 
                                bd=0, activebackground='#5271ff', command=lambda: self.indicator(indi_lbl=home_ind, page_switch=self.home))
          home_button.place(x=6, y=100, height=40, width=30) 

          home_ind = Label(menu_bar, bg='white')
          home_ind.place(x=3, y=100, height=40, width=3)

          home_label = Label(menu_bar, text='Home', bg='#5271ff', fg='white',
                            font=('Arial', 15), anchor=W)
          home_label.place(x=45, y=100, width=100, height=40)
          home_label.bind('<Button-1>', lambda e: self.indicator(indi_lbl=home_ind, page_switch=self.home ))

            #methods icon
          methods_button = Button(menu_bar, image=methods_icon, bg='#5271ff', 
                                    bd=0, activebackground='#5271ff', command=lambda: self.indicator(indi_lbl=method_ind, page_switch=self.methods))
          methods_button.place(x=6, y=170, height=40, width=30)

          method_ind = Label(menu_bar, bg='#5271ff')
          method_ind.place(x=3, y=170, height=40, width=3)

          method_label = Label(menu_bar, text='Models', bg='#5271ff', fg='white',
                        font=('Arial', 15), anchor=W)
          method_label.place(x=45, y=170, width=120, height=40)
          method_label.bind('<Button-1>', lambda e: self.indicator(indi_lbl=method_ind, page_switch=self.methods))

            #info_icon
          info_button = Button(menu_bar, image=info_icon, bg='#5271ff',
                                bd=0, activebackground='#5271ff', command=lambda: self.indicator(indi_lbl=info_ind, page_switch=self.info))
          info_button.place(x=6, y=240, height=40, width=30)

          info_ind = Label(menu_bar, bg='#5271ff')
          info_ind.place(x=3, y=240, height=40, width=3)

          info_label = Label(menu_bar, text='Info', bg='#5271ff', fg='white',
                        font=('Arial', 15), anchor=W)
          info_label.place(x=45, y=240, width=100, height=40)
          info_label.bind('<Button-1>', lambda e: self.indicator(indi_lbl=info_ind, page_switch=self.info))

            #account_icon
          account_button = Button(menu_bar, image=account_icon, bg='#5271ff', bd=0, 
                            activebackground='#5271ff', command=lambda: self.indicator(indi_lbl=account_ind))
          account_button.place(x=6, y=310, height=40, width=30)

          account_ind = Label(menu_bar, bg='#5271ff')
          account_ind.place(x=3, y=310, height=40, width=3)

          account_label = Label(menu_bar, text='Account', bg='#5271ff', fg='white',
                        font=('Arial', 15), anchor=W)
          account_label.place(x=45, y=310, width=120, height=40)
          account_label.bind('<Button-1>', lambda e: self.indicator(indi_lbl=account_ind))

          menu_bar.pack(side=LEFT, fill=Y, padx=3, pady=4)
          menu_bar.pack_propagate(flag=False)

          menu_bar.configure(width=45)

     def indicator(self, indi_lbl, page_switch):
          self.home_ind.config(bg='#5271ff')
          self.info_ind.config(bg='#5271ff')
          self.method_ind.config(bg='#5271ff')
          self.account_ind.config(bg='#5271ff')

          indi_lbl.config(bg='white')
          if self.menu_bar.winfo_width() > 45:
                self.fold_menu()

          for frame in page.winfo_children():
               frame.destroy()
               page_switch()

     def animate_menu(self):
           self.current_width = self.menu_bar.winfo_width()
           if not current_width > 200:
                current_width += 10
                self.menu_bar.config(width=current_width)
                
                root.after(ms=8, func=self.animate_menu)

     def extend_menu(self):
           self.animate_menu()
           self.toggle_button.config(image=close_icon)
           self.toggle_button.config(command=self.fold_menu)

     def animate_folding(self):
           current_width = self.menu_bar.winfo_width()
           if current_width != 45:
                 current_width -= 10
                 self.menu_bar.config(width=current_width)
                 
                 root.after(ms=8, func=self.animate_folding)

     def fold_menu(self):
           self.animate_folding()
           self.toggle_button.config(image=toggle_icon)
           self.toggle_button.config(command=self.extend_menu)

     def home(self):
           h_page=Frame(page)
           lb = Label(h_page, image=wallp)
           lb.pack()
           
           h_page.pack(fill=BOTH, expand=True)

    
     def methods(self):
      #labels
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

     def info(self):
      i_page=Frame(page)
      lb = Label(i_page, text='This is a Rock Fragmentation App \nMade by Central South University foreign student', font=('Times new Roman', 12,))
      lb.place(x=100, y=200)

      i_page.pack(fill=BOTH, expand=True)


    #  page = Frame(root, bg='#D8D2C2')
    #  page.place(relheight=1.0, relwidth=1.0, x=50)
    #  home()
    #  methods()
    #  info()

page = Sign_in(root)

#run 
root.mainloop()