

---
## 📌 Note

**This project is made for educational purposes only. Do not use it for storing sensitive or real-world passwords without proper encryption and security measures.**

---
# 🔐 Password Manager

- This **Password Manager** is a simple yet powerful GUI-based Python application built using **Tkinter**.  
- It is part of my **learning journey** to explore Python, GUI programming, and file handling.  
- The tool allows users to generate strong passwords, save them to a MongoDB Atlas.

---

## 🚀 Features

- ✅ **Generate Password**: Instantly generate strong random passwords.
- 💾 **Save Password**: Save app name, username, and generated password to a Database.
- 🧹 **Clear Fields**: Clear all input fields with a single click.
- ❌ **Delete Data**: Permanently delete all saved passwords from the CSV file.
- 📋 **Copy Password**: Quickly copy the generated password to clipboard for easy use.
- **Login** : Login with username and password to access the dashboard.
- **database integration** Stores your password and username in databse for security.

---

## 📁 File Structure

```
password_manager/
│
├── main.py # Main script to run the application
├── .gitignore 
└── README.md # Project documentation
|__ .env # stores MongoDB string
```
---

---

## 📚 Libraries Used

- `tkinter` – for creating the GUI
- `random` – for generating random password characters
- `string` – for accessing letters, digits, and punctuation sets
- `pymongo` - for handling mongodb to store data and errors.
- `dotenv` - to load MongoDB string from .env file

---
