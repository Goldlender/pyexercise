import tkinter as tk  
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
#from PIL import Image, ImageTk
#import customtkinter as ctk

root = Tk()
root.title('Sign In')
root.geometry('400x400')
root.configure(bg='#B7B7B7')


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


page = Sign_in(root)

#run 
root.mainloop()
