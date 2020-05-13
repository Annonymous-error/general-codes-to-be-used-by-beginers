# -*- coding: utf-8 -*-
"""
Created on Tue May  5 00:05:41 2020
tabs in gui app
menu baar tutuorial
@author: Ayush Gupta
"""


import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('menubar with tabs')

############################
nb=ttk.Notebook(win)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text='one')
nb.add(page2,text='Two')
# nb.grid(row=0,column=0)
nb.pack(expand=True,fill='both')
label1=ttk.Label(page1,text='this is tabbed app')
label1.grid(row=0,column=0)
###############################

def func():
    print('func called')


# menubar=tk.Menu(win)     simple menu bar
# menubar.add_command(label='File',command=func)
# menubar.add_command(label='Edit',command=func)
# win.config(menu=menubar)
    
    
main_menu = tk.Menu(page1)
file_menu = tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New file',command=func)
file_menu.add_separator()
file_menu.add_command(label='New window',command=func)  
main_menu.add_cascade(label='File',menu=file_menu) 



edit_menu=tk.Menu(main_menu,tearoff=0)
edit_menu.add_cascade(label='undo',command=func)

main_menu.add_cascade(label='Edit',  menu=edit_menu)


win.config(menu=main_menu)
win.mainloop()

 