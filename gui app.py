# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:18:27 2020
how to create gui

@author: Ayush Gupta

"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from csv import DictWriter
import os
win = tk.Tk()
win.title('Gui')
#creating lables
name_label=ttk.Label(win,text='Enter your name')
name_label.configure(foreground='#80cbc4')  #hex value from google colour picker
name_label.grid(row=0, column=0,sticky=tk.W )


age_label=ttk.Label(win,text='Enter your age')
age_label.grid(row=1,column=0,sticky=tk.W)

email_label=ttk.Label(win,text='Enter your email')
email_label.grid(row=2,column=0,sticky=tk.W)

#entry boxes
name_var= tk.StringVar()
name_entrybox = ttk.Entry(win,width=16,textvariable= name_var)
name_entrybox.grid(row=0, column=1)


age_var= tk.StringVar()
age_combobox = ttk.Combobox(win,width=16,textvariable=age_var,state='readonly')
age_combobox['values']=tuple([str(i) for i in range(10,50)])
age_combobox.current(1)
age_combobox.grid(row=1, column=1 )

email_var= tk.StringVar()
email_entrybox = ttk.Entry(win,width=22,textvariable= email_var)
email_entrybox.grid(row=2, column=1)

# radio button
usertype=tk.StringVar()
rbtn1=ttk.Radiobutton(win,text='student',value='student',variable=usertype)
rbtn1.grid(row=4,column=0)
rbtn2=ttk.Radiobutton(win,text='teacher',value='teacher',variable=usertype)
rbtn2.grid(row=4,column=1)


# check button
checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text='check if you want to subscribe',variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)

# create button
def action():             #action to be performed when submit is pressed
            username=name_var.get()
            userage=age_var.get()
            useremail= email_var.get()
            print(f'{username} is {userage} years old,{useremail}')
            userage=age_var.get()
            user_type=usertype.get()
            if checkbtn_var.get()==0:
                subscribed='NO'
            else:
                subscribed='YES'
                
            with open ('fileg.csv','a',newline='') as f:        
                dict_writer=DictWriter(f, fieldnames=['Username','Userage','email','usertype','Subscribed'])
                if os.stat('fileg.csv').st_size==0 :
                    dict_writer.writeheader()
                dict_writer.writerow({'Username':username,
                                          'Userage':userage,
                                          'email':useremail,
                                          'usertype':user_type,
                                          'Subscribed':subscribed
                                          })
            # with open ('filegui.txt','r+') as f:
               # f.write(f'\n {username},{userage},{useremail},{user_type},{subscribed}')     
            mbox.showinfo('voila','you agreed')#showerror  ,showwrningd
            name_entrybox.delete(0,tk.END)
            age_combobox.delete(0,tk.END)
            email_entrybox.delete(0,tk.END)
            

submit_button=tk.Button(win,text='Submit',command=action)
submit_button.configure(foreground='Blue')
submit_button.grid(row=6,column=1)

name_entrybox.focus()
win.mainloop()  # to open window




