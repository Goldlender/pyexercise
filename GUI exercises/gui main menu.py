import tkinter as tk  
from tkinter import ttk

win = tk.Tk()

win.title('Rock Fragmentation App')

# model_selection = ttk.Label(win, text='Choose model')
# model_selection.grid(column=0, row=0)

#ADDING A TEXTBOX ENTRY WIDGET
# name = tk.StringVar()
# name_entered = ttk.Entry(win, width=12, textvariable=name)
# name_entered.grid(column=0, row=0)


#button click event function 
def click_me():
    action.configure(text = 'Done!')
    # model_selection.configure(foreground='red')
    # model_selection.configure(text='Model')

# adding a button 
action = ttk.Button(win, text='Confirm', command=click_me)
action.grid(column=1, row=1)
#action.configure(state='disabled')

#combobox widget
ttk.Label(win, text = 'Select a Model').grid(column=0, row=0)
model = tk.StringVar()
model_chosen = ttk.Combobox(win, width=12, textvariable=model)
model_chosen['values']= ('RF model', 'HGB_model','XGBoost', 'ET model')
model_chosen.grid(column=0, row=1)
model_chosen.current(0)

# name_entered.focus()     #place cursor into name entry


win.mainloop()