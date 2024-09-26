import tkinter as tk  
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title('RF App')
root.geometry('800x800')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

class App:

    def __init__(self, master):
        #frames
        myframe = Frame(master, bg='#B7B7B7')
        theframe = LabelFrame(master, text='Initialization', bg='#B7B7B7')
        myframe.grid(column=0, row=0, sticky='news', pady=5, padx=20)
        theframe.grid(column=0, row=1, sticky='news', pady=5, padx=20)
        theframe1 = LabelFrame(master, text='Hyperparameter & Dataset Partition', bg='#B7B7B7')
        theframe1.grid(column=0, row=3, sticky='news', pady=5, padx=20)
        theframe2 = LabelFrame(master, text='Training Set Performance', bg='#B7B7B7')
        theframe2.grid(column=0, row=5, sticky='news', pady=5, padx=20)
        theframe3 = LabelFrame(master, text='Testing Set Performance', bg='#B7B7B7')
        theframe3.grid(column=0, row=6, sticky='news', pady=5, padx=20)
        theframe4 = LabelFrame(master, text='Model Explanability & Analysis', bg='#B7B7B7')
        theframe4.grid(column=0, row=7, columnspan=1, rowspan=7,sticky='nw', padx=5, pady=20)
        theframe5 = LabelFrame(master, text='Plots', bg='#B7B7B7')
        theframe5.config()
        theframe5.grid(column=0, row=7,columnspan=2, rowspan=7,sticky='nse', padx=5, pady=20)

        #menu
        menu_bar = Menu(master)
        root.config(menu=menu_bar)

        #plots
        fig, ax = plt.subplots(figsize=(4, 4))

        canvas = FigureCanvasTkAgg(fig, master = theframe5)
        canvas.get_tk_widget().grid()



        mylabel = Label(myframe, text = 'Input Data:')
        mylabel.grid(column=0, row=0,pady=5, padx=5)
        myentry = Entry(myframe, width=35)
        myentry.grid(column=1, row=0, pady=5, padx=5)

        #buttons
        mybutton1 = Button(myframe, text='Load Data', command=self.click).grid(column=2, row=0, pady=5, padx=5)
        mybutton2 = Button(myframe, text='Train/Test', command=self.click).grid(column=3, row=0, pady=5, padx=5)
        mybutton3 = Button(myframe, text='Analyze Results', command=self.click).grid(column=4, row=0, pady=5, padx=5)
        mybutton4 = Button(myframe, text='Predict', command=self.click).grid(column=5, row=0, pady=5, padx=5)
        mybutton4 = Button(myframe, text='Main Menu', command=self.click).grid(column=6, row=0, pady=5, padx=5)

        #label frame widgets
        mylabel = Label(theframe, text='Test size').grid(column=0, row=2, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe, width=10, textvariable=name)
        name_entered.grid(column=1, row=2, padx=7, pady=7)

        mylabel= Label(theframe, text='Swarm size').grid(column=2, row=2, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe, width=10, textvariable=name)
        name_entered.grid(column=3, row=2, padx=7, pady=7)

        mylabel= Label(theframe, text='Lower bound').grid(column=4, row=2, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe, width=10, textvariable=name)
        name_entered.grid(column=5, row=2, padx=7, pady=7)

        mylabel= Label(theframe, text='Upper bound').grid(column=6, row=2, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe, width=10, textvariable=name)
        name_entered.grid(column=7, row=2, padx=7, pady=7)

        #label frame1 widgets
        mylabel= Label(theframe1, text='n_estimators').grid(column=8, row=4, padx=3, pady=3)
        name = tk.StringVar()
        name_entered = Entry(theframe1, width=10, textvariable=name)
        name_entered.grid(column=9, row=4, padx=7, pady=7)

        mylabel= Label(theframe1, text='Max_depth').grid(column=10, row=4, padx=3, pady=3)
        name = tk.StringVar()
        name_entered = Entry(theframe1, width=10, textvariable=name)
        name_entered.grid(column=11, row=4, padx=7, pady=7)

        mylabel= Label(theframe1, text='Fitness').grid(column=12, row=4, padx=3, pady=3)
        name = tk.StringVar()
        name_entered = Entry(theframe1, width=10, textvariable=name)
        name_entered.grid(column=13, row=4, padx=3, pady=3)

        mylabel= Button(theframe1, text='Iterations', command=self.click).grid(column=14, row=4, padx=7, pady=7)
        mylabel= Button(theframe1, text='Training set', command=self.click).grid(column=15, row=4, padx=7, pady=7)
        mylabel= Button(theframe1, text='Testing set', command=self.click).grid(column=16, row=4, padx=7, pady=7)

        #label frame2 widgets
        mylabel= Label(theframe2, text='RMSE').grid(column=0, row=5, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe2, width=10, textvariable=name)
        name_entered.grid(column=1, row=5, padx=2, pady=4)

        mylabel= Label(theframe2, text='MSE').grid(column=2, row=5, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe2, width=10, textvariable=name)
        name_entered.grid(column=3, row=5, padx=7, pady=7)

        mylabel= Label(theframe2, text='MAE').grid(column=4, row=5, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe2, width=10, textvariable=name)
        name_entered.grid(column=5, row=5, padx=2, pady=4)

        mylabel= Label(theframe2, text='R2').grid(column=6, row=5, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe2, width=10, textvariable=name)
        name_entered.grid(column=7, row=5, padx=7, pady=7)

        mylabel= Button(theframe2, text='Save Results', command=self.click).grid(column=8, row=5, padx=7, pady=7)

        #label frame 3 widgets
        mylabel= Label(theframe3, text='RMSE').grid(column=0, row=6, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe3, width=10, textvariable=name)
        name_entered.grid(column=1, row=6, padx=7, pady=7)

        mylabel= Label(theframe3, text='MSE').grid(column=2, row=6, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe3, width=10, textvariable=name)
        name_entered.grid(column=3, row=6, padx=7, pady=7)

        mylabel= Label(theframe3, text='MAE').grid(column=4, row=6, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe3, width=10, textvariable=name)
        name_entered.grid(column=5, row=6, padx=7, pady=7)

        mylabel= Label(theframe3, text='R2').grid(column=6, row=6, padx=7, pady=7)
        name = tk.StringVar()
        name_entered = Entry(theframe3, width=10, textvariable=name)
        name_entered.grid(column=7, row=6, padx=7, pady=7)

        mylabel= Button(theframe3, text='Save Results', command=self.click).grid(column=8, row=6, padx=7, pady=7)

        #labels frame 4
        mylabel= Label(theframe4, text='Feature Importance').grid(column=0, row=7, padx=7, pady=7)
        mylabel= Label(theframe4, text='LIME Analysis').grid(column=0, row=8, padx=7, pady=7)
        mylabel= Label(theframe4, text='SHAP Analysis').grid(column=0, row=9, padx=7, pady=7)

        mylabel= Button(theframe4, text='Save Image', command=self.click).grid(column=2, row=7, padx=7, pady=7)
        mylabel= Button(theframe4, text='Save Data', command=self.click).grid(column=1, row=7, padx=7, pady=7)
        mylabel= Button(theframe4, text='Save Data', command=self.click).grid(column=2, row=8, padx=7, pady=7)
        mylabel= Button(theframe4, text='Save Graph', command=self.click).grid(column=2, row=9, padx=7, pady=7)

        #LIME
        name = tk.StringVar()
        name_entered = Entry(theframe4, width=10, textvariable=name)
        name_entered.grid(column=1, row=8, padx=7, pady=7)

        #SHAP
        name = tk.StringVar()
        name_entered = Entry(theframe4, width=10, textvariable=name)
        name_entered.grid(column=1, row=9, padx=7, pady=7)

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
        file_menu.add_command(label='Exit')
        menu_bar.add_cascade(label ='File', menu=file_menu)

        

    def click(self):
        print('someone clicked me')
 

app = App(root)



#RUN
root.mainloop()