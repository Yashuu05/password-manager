# importing modules
import tkinter as tk
import string
import random
from tkinter import messagebox
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.errors import DuplicateKeyError, ConnectionFailure
#-----------------------------------------------------

# load data from .env file
load_dotenv()
# Read MongoDB URI from environment
mongo_uri = os.getenv("MONGO_URI")
# create client to connect to your MongoDB Atlas string
client = MongoClient(mongo_uri)

# select your database name and collection name
db = client["password_manager"]
users_collection = db['users']

# function for password manager dashboard
def pass_manager_dashboard():
    # withdraw the login window
    window.withdraw()
    # create a window
    root = tk.Toplevel()
    # title for window
    root.title('password generator')
    # size of window
    root.geometry('600x300')
    # set background color
    root.config(bg='black')

    #-------------------------------------------------------
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

    #-------------------------------------------
    # function to copy the password
    def copy():
        root.clipboard_clear()
        root.clipboard_append(password_entry.get())
        messagebox.showinfo('message','password copied')

    #----------------------------------------------
    # function to clear the imput field
    def clear():
        password_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        app_name_entry.delete(0, tk.END)

    #-----------------------------------------------
    # function to delete all passwords
    def delete(): 
        ########################################
        # create a new window inside the delete()
        delete_win = tk.Toplevel()
        # title of window
        delete_win.title('Delete')
        # geometry
        delete_win.geometry('300x180')
        # background color:
        delete_win.config(bg='black')

        # function to delete the data
        def delete_data():

            try:
                with open('passwords.csv','r') as file:
                    first_line = file.readline()
                with open('passwords.csv','w') as f:
                    f.write(first_line)
                messagebox.showinfo('Info','all data deleted')
                delete_win.destroy()
            except FileExistsError:
                messagebox.showerror('No file exist!')
            except FileNotFoundError:
                messagebox.showerror('No file found!')

        # function to go back
        def back():
            delete_win.destroy()
    
        # delete window widgets
        # =============================================
        # heading 
        tk.Label(delete_win, text='Delete permanently?', font=('Arial',14,'bold'), bg='black', fg='white').pack(pady=10)
        # delete button
        tk.Button(delete_win, text='Yes', font=('Georgia',9,'bold'), bg='#FF4F0F', fg='white',command=delete_data, width=12).pack(pady=10)
        # back button
        tk.Button(delete_win, text='No', font=('Georgia',9,'bold'), bg='#B6F500', command=back,width=12).pack(pady=10)
        #####################################################

    """
    def save():

        try:
            with open('passwords.csv','a') as file:
                app_name = app_name_entry.get()
                username = username_entry.get()
                password = password_entry.get()
                data = ['\n',app_name,',',username,',',password]
                file.writelines(data)
            messagebox.showinfo('info','data saved successfully!')
            # delete all data
            password_entry.delete(0, tk.END)
            username_entry.delete(0, tk.END)
            app_name_entry.delete(0, tk.END)
        except FileNotFoundError:
            messagebox.showerror('Error','File Not found!')
        except FileExistsError:
            messagebox.showerror('Error!','File not exist!')
    """
    def save():
        app_name = app_name_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        entry = {
            "app name" : app_name,
            "username" : username,
            "password" : password,
        }
        try:
            # insert the entry into database
            users_collection.insert_one(entry)
            # alert user
            messagebox.showinfo('message','data saved successfully')
        except ConnectionFailure:
            messagebox.showerror("Error","Oops! Cannot connect to Database. Check Network Connection")
        except DuplicateKeyError:
            messagebox.showerror("Error","This app's credentials already exist.")
        except ConnectionError:
            messagebox.showerror('Error','Connection Failed!')

    def logout():
        root.destroy()
        window.deiconify()
# ---------------------------------------------------------------------------------------------------------------------------

    # create a label for heading
    tk.Label(root, text='welcome to password generator!', bg='black',fg='white', font=('Georgia',12,'bold')).grid(row=0, column=0, columnspan=3,padx=10,pady=10)

    # button to generate the password
    tk.Button(root, text='generate password',command=password_generate,font=('Georgia',10,'bold'), bg='#EBD6FB').grid(row=2,column=2, padx=10, pady=10)

    # create the entry for generating a password
    password_entry = tk.Entry(root, bd=2, width=30, bg='#DDDDDD')
    password_entry.grid(row=3,column=1,padx=10, pady=10)
    #password_entry.config(state='readonly')

    # button for copy
    tk.Button(root, text='copy password', command=copy, font=('Georgia',10,'bold'), bg='#8CCDEB').grid(row=4,column=1,padx=10,pady=10)

    # button to clear
    tk.Button(root, text='clear', command=clear, font=('Georgia',10,'bold'), bg='#feb236').grid(row=4,column=0, padx=10, pady=10)

    # button to delete
    tk.Button(root, text='Delete data', command=delete, font=('Georgia',10,'bold'), bg="#FF4F0F", fg='white', width=16).grid(row=3, column=2, pady=10, padx=10) 

    # button to save data
    tk.Button(root, text='Save', command=save, font=('Georgia',10,'bold'), bg='#B6F500', width=15).grid(row=4, column=2, pady=10, padx=10) 

    # button for logout
    tk.Button(root, text="logout", command=logout, font=('Georgia',10, 'bold'), bg="#DDDDDD", width=15).grid(row=1, column=2, pady=10, padx=10)

    # creating a label for app name:
    app_name_label = tk.Label(root, text='App Name', bg='black', font=('Arial',11,'bold'), fg='white')
    app_name_label.grid(row=1, column=0,pady=10, padx=10)

    # creating label for username:
    username_label = tk.Label(root, text='Username', bg='black', font=('Arial',11,'bold'), fg='white')
    username_label.grid(row=2, column=0,pady=10, padx=10)

    # creating label for password
    password_label = tk.Label(root, text='Password', bg='black', font=('Arial',11,'bold'), fg='white')
    password_label.grid(row=3, column=0,pady=10, padx=10)

    # entry field for app name
    app_name_entry = tk.Entry(root, bd=2, width=30, bg='#DDDDDD')
    app_name_entry.grid(row=1, column=1, padx=10, pady=10)

    # entry for username
    username_entry = tk.Entry(root, bd=2, width=30, bg='#DDDDDD')
    username_entry.grid(row=2, column=1, padx=10, pady=10)

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# PROGRAM FOR LOGIN WINDOW

# create login window
window= tk.Tk()
# title for window
window.title('login')
# geometry 
window.geometry('350x250')
# background color
window.config(bg='black')
# login logic
def login():
    # get user input from input fields
    username = username_entry.get()
    password = pass_entry.get()
    try:
        user = users_collection.find_one({"username": username, "password": password})
        if user:
            messagebox.showinfo('info','login successful')
            username_entry.delete(0, tk.END)
            pass_entry.delete(0, tk.END)
            # open password manager window
            pass_manager_dashboard()
        elif username == '' and password == '':
            messagebox.showerror('Error','Enter Credentials to proceed')
        else:
            messagebox.showerror('Error','invalid credentials')
    except ConnectionFailure:
        messagebox("Eorror"," cannot connect to database")
    except ConnectionError:
        messagebox("Error","Connection Error!")

# heading label
heading = tk.Label(window, text='welcome!', font=('Georgia',18,'italic'), fg='white', bg='black').grid(row=0, column=1, pady=20)

# username label
username_label = tk.Label(window, text="Username", font=('Arial',10,'bold'), fg='white', bg='black')
username_label.grid(row=1, column=0, pady=10, padx=10)
# usermame entry
username_entry = tk.Entry(window, bd=2, width=20)
username_entry.grid(row=1, column=1, padx=10, pady=10)

# password label
pass_label = tk.Label(window, text="Password", font=('Arial',10,'bold'), bg='black', fg='white')
pass_label.grid(row=2, column=0, pady=10, padx=10)
# password entry
pass_entry = tk.Entry(window, bd=2, width=20)
pass_entry.grid(row=2, column=1, padx=10, pady=10)

# login button
login_btn = tk.Button(window, text='Login', command=login, font=('Arial',10,'bold'), bg='#00FFDE',width=10).grid(row=3, column=1, pady=10, padx=10)

# run winodw
window.mainloop()