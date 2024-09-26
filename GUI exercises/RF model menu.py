import tkinter as tk  
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

class RF_App(tk.Tk):
    def __init__(self, title, size):

        #main setup
        super().__init__()
        self.title('Random Forest model')
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        
        #widgets
        self.main1 = Main1(self)
        self.main2 = Main2(self)
        

        self.mainloop()



class Main1(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=8, relheight=4)

        self.create_widgets()

     #button click event function 
    def click_me(self):
        self.action.configure()

    def create_widgets(self):
        ttk.Label(self, text='Data path:').grid(column=0, row=0, padx=4, pady=4)
        name = tk.StringVar(self)
        name_entered = ttk.Entry(self, width=12, textvariable=name)
        name_entered.grid(column=1, row=0, padx=4, pady=4)

        action = ttk.Button(self, text='Load Data', command=self.click_me)
        action.grid(column=2, row=0, padx=4, pady=4)
        action = ttk.Button(self, text='Train/Test', command=self.click_me)
        action.grid(column=3, row=0, padx=4, pady=4)
        action = ttk.Button(self, text='Results', command=self.click_me)
        action.grid(column=4, row=0, padx=4, pady=4)
        action = ttk.Button(self, text='Predict', command=self.click_me)
        action.grid(column=5, row=0, padx=4, pady=4)
        action = ttk.Button(self, text='Main menu', command=self.click_me)
        action.grid(column=6, row=0, padx=4, pady=4)



class Main2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #Add Label Frame
        b_frame = ttk.LabelFrame(self, text = 'Initialize Settings').grid(column=1, row=3)

        #test size label
        ttk.Label(b_frame, text='Test size').grid(column=1, row=4, sticky=tk.W)
        name = tk.StringVar()
        name_entered = ttk.Entry(b_frame, width=10, textvariable=name)
        name_entered.grid(column=2, row=4, padx=2, pady=4)

        #swarm size label
        ttk.Label(b_frame, text='Swarm size').grid(column=3, row=4, sticky=tk.W)
        name = tk.StringVar()
        name_entered = ttk.Entry(b_frame, width=10, textvariable=name)
        name_entered.grid(column=4, row=4, padx=2, pady=4)

        #lower boundary
        ttk.Label(b_frame, text='Lower Bound').grid(column=1, row=6, sticky=tk.W)
        name = tk.StringVar()
        name_entered = ttk.Entry(b_frame, width=10, textvariable=name)
        name_entered.grid(column=2, row=6, padx=2, pady=4)

        #upper boundary
        ttk.Label(b_frame, text='Upper Bound').grid(column=3, row=6, sticky=tk.W)
        name = tk.StringVar()
        name_entered = ttk.Entry(b_frame, width=10, textvariable=name)
        name_entered.grid(column=4, row=6, padx=2, pady=4)



    
# #Add Label Frame
#     b_frame = ttk.LabelFrame(self.win, text = 'Initialize Settings')
#     b_frame.grid(column=0, row=1, padx=4, pady=4)

# #test size label
#     ttk.Label(b_frame, text='Test size').grid(column=1, row=0, sticky=tk.W)
#     name = tk.StringVar()
#     name_entered = ttk.Entry(b_frame, width=10, textvariable=name)
#     name_entered.grid(column=2, row=0, padx=2, pady=4)

# #swarm size label
#     ttk.Label(b_frame, text='Swarm size').grid(column=3, row=0, sticky=tk.W)
#     name = tk.StringVar()
#     name_entered = ttk.Entry(b_frame, width=10, textvariable=name)
#     name_entered.grid(column=4, row=0, padx=2, pady=4)

# #lower boundary
#     ttk.Label(b_frame, text='Lower Bound').grid(column=3, row=1, sticky=tk.W)
#     name = tk.StringVar()
#     name_entered = ttk.Entry(b_frame, width=10, textvariable=name)
#     name_entered.grid(column=2, row=1, padx=2, pady=4)

# #upper boundary
# ttk.Label(b_frame, text='Upper Bound').grid(column=1, row=1, sticky=tk.W)
# name = tk.StringVar()
# name_entered = ttk.Entry(b_frame, width=10, textvariable=name)
# name_entered.grid(column=4, row=1, padx=2, pady=4)

# # #Exit GUI
# def _quit(self):
#     self.win.quit()
#     self.win.destroy()
#     exit()

# #creating a menu bar
# menu_bar = Menu(win)
# win.config(menu=menu_bar)

#create menu and add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New File')
file_menu.add_command(label='Open File')
file_menu.add_separator()
file_menu.add_command(label='Save File')
file_menu.add_command(label='Save File As')
file_menu.add_separator()
file_menu.add_command(label='Export')
file_menu.add_command(label='Recent Export')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label ='File', menu=file_menu)

# #Display a message box 
# def msgbox():
#     # msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:'
#     # '\n The year is 2024!')
#     # msg.showwarning('Python Message Warning Box', 
#     # 'A Python GUI created using tkinter:'
#     # '\nWarning: There might be a bug in this code!')
#     # msg.showerror('Python Message Error Box', 
#     # 'A python GUI created using tkinter:'
#     # '\nError: There is an Error')
#     answer = msg.askyesnocancel('Python Message Multi Choice Box', 'Are you sure?')
#     print(answer)
# #creating a help menu
# help_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label='Help', menu=help_menu)
# help_menu.add_command(label='About', command=msgbox)

# #changing icon
# #win.iconbitmap('')
# name_entered.focus()

#self.mainloop()
RF_App('class_based', (700, 700))