# importing modules
import tkinter as tk
import string
import random
from tkinter import messagebox
#-----------------------------------------------------
# create a window
root = tk.Tk()
# title for window
root.title('password generator')
# size of window
root.geometry('500x200')
# set background color
root.config(bg='black')
# create a label for heading
tk.Label(root, text='welcome to password generator!', bg='black',fg='white', font=('Georgia',12,'bold')).grid(row=0, column=0, columnspan=2,padx=10,pady=10)
# function to generate random passwords
def password_generate():
    s = string.ascii_letters + string.punctuation + string.digits
    i = 1
    password = ''
    while i < 11:
        y = random.choice(s)
        password += y
        i += 1
    password = password
    # create the entry for generated password
    password_entry.config(state='normal')
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    #password_entry.config(state='readonly')

# function to copy the password
def copy():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())

# function to clear the imput field
def clear():
    password_entry.delete(0, tk.END)

# button to generate the password
tk.Button(root, text='generate password',command=password_generate,font=('Georgia',10,'bold'), bg='#EBD6FB').grid(row=1,column=0, padx=10, pady=10)

# create the entry for generating a password
password_entry = tk.Entry(root, font=('Courier',10), justify='center',width=30)
password_entry.grid(row=1,column=1,padx=10, pady=10)
#password_entry.config(state='readonly')

# button for copy
tk.Button(root, text='copy', command=copy, font=('Georgia',10,'bold'), bg='#82b74b').grid(row=2,column=1,padx=10,pady=10)

# button to clear
tk.Button(root, text='clear', command=clear, font=('Georgia',10,'bold'), bg='#feb236').grid(row=2,column=0, padx=10, pady=10)

# run the window
root.mainloop()