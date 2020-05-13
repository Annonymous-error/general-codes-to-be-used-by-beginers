# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:02:14 2020
how to create label_frame 
@author: Ayush Gupta
"""


import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Gui_LABELFRAME')
label_frame=ttk.LabelFrame(win,text='enter details')
label_frame.grid(row=0,column=0,padx=850,pady=350)

labels=['what is your name:','what is your age:','country:']
for i in range(len(labels)):
    current_label='label'+str(i)
    current_label=ttk.Label(label_frame ,text=labels[i])
    current_label.grid(row=[i],column=0,sticky=tk.W,padx=2,pady=2)


name_var=tk.StringVar()
user_info = {
    'name': tk.StringVar(),
    'age':tk.StringVar(),
    'country':tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox='entry'+i
    cur_entrybox=ttk.Entry(label_frame,width=16,textvariable=user_info[i])
    cur_entrybox.grid(column=1,row=counter,padx=2,pady=2)
    counter+=1
    
    
def submit():
        print(user_info['name'].get())
        print(user_info.get('age'))
        print(user_info.getU('country'))
        
submit_btn=ttk.Button(win,text='submit',command=submit)
submit_btn.grid(row=1,columnspan=1)
win.mainloop()

# for child in label_frame.winfo_children():
    # child.grid_configure(padx=4,pady=4)









win.mainloop()    