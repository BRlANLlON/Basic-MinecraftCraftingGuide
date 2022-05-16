from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("forum")
root.configure(bg="#bb7f10")
root.geometry("500x500")

bg = PhotoImage(file = "C:/Users/brian/OneDrive/Desktop/project/free.png")
back=Label(root, image = bg)
back.place(x=0, y=0)

#icon
icon = PhotoImage(file = "logo.png")
root.iconphoto(False, icon)

#frame that holds everything center
frame_1 = tk.Frame(root, bg="#AF824D", height = "350", width = "350")
frame_1.pack(side=tk.BOTTOM)
frame_1.place(relx=0.5, rely=0.5, anchor = (tk.CENTER))

#frame2
frame_2 = tk.Frame(frame_1, width=100, height=20, bg="#AF824D")
frame_2.pack(side = tk.BOTTOM)


#frame3
frame_3 = tk.Frame(frame_1, width=300, height=300, bg="#AF824D")
frame_3.pack(side = tk.TOP)


#string entry
username_var = tk.StringVar()
first_var = tk.StringVar()
last_var = tk.StringVar()
email_var = tk.StringVar()
passw_var = tk.StringVar()

#defining the variables with user input
def submit():
    username = username_var.get()
    username_var.set("")
    
    first_name = first_var.get()
    first_var.set("")
    
    last_name = last_var.get()
    last_var.set("")

    email_address = email_var.get()
    email_var.set("")
    
    password = passw_var.get()
    passw_var.set("")

    #check if entry works in shell
    print("Your name is: " + first_name + " " + last_name)
    print("Your email is: " + email_address)
    print("The username is: " + username)
    print("The password is set to: " + password)

    #saves info in text file
    file = open("forum.txt", "w")
    file.write(username)
    file.write(first_name)
    file.write(last_name)
    file.write(email_address)
    file.write(password)
    file.close()

    #deletes entry for next user
    username_entry.delete(0, END)
    first_entry.delete(0, END)
    last_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)



#once creating an account, logging in and opening another window
def login():
    user = username_var.get()
    first = first_var.get()
    last = last_var.get()
    email = email_var.get()
    password = passw_var.get()

    if user == username_var.get() and first == first_var.get() and last == last_var.get() and email == email_var.get() and password == passw_var.get():
        print("logged in")
    if not username_var.get():
        print("Your information is not correct")

#clearing
def clear():
    username_entry.delete(0, 1000)
    first_entry.delete(0, 1000)
    last_entry.delete(0, 1000)
    email_entry.delete(0, 1000)
    password_entry.delete(0, 1000)


#inside frame 2
#creating entry with labels
username_label = tk.Label(frame_3, text = "Username", bg="#d7b465", fg="#221305", font=("Microsft YaHei UI Light", 10, "bold"))
username_entry = tk.Entry(frame_3, textvariable = username_var, font=("open sans", 10, "normal"), relief=SUNKEN)

first_label = tk.Label(frame_3, text = "First Name", bg="#d7b465", fg="#221305", font=("Microsft YaHei UI Light", 10, "bold"))
first_entry = tk.Entry(frame_3, textvariable = first_var, font=("open sans", 10, "normal"), relief=SUNKEN)

last_label = tk.Label(frame_3, text = "Last Name", bg="#d7b465", fg="#221305", font=("Microsft YaHei UI Light", 10, "bold"))
last_entry = tk.Entry(frame_3, textvariable = last_var, font=("open sans", 10, "normal"), relief=SUNKEN)

email_label = tk.Label(frame_3, text = "Email", bg="#d7b465", fg="#221305", font=("Microsft YaHei UI Light", 10, "bold"))
email_entry = tk.Entry(frame_3, textvariable = email_var, font=("open sans", 10, "normal"), relief=SUNKEN)

password_label = tk.Label(frame_3, text = "Password", bg="#d7b465", fg="#221305", font=("Microsft YaHei UI Light", 10, "bold"))
password_entry = tk.Entry(frame_3, textvariable = passw_var, font=("open sans", 10, "normal"), relief=SUNKEN)

#create buttons and commands
log_btn= tk.Button(frame_2,text = "Login", command = login, bg="#4A6F28", fg="black", relief=RAISED)
create_btn= tk.Button(frame_2,text = "Create an Account", command = submit, bg="#664c3f", fg="white", relief=RAISED)
clear_btn= tk.Button(frame_2,text = "Clear", command = clear, bg="#858A7E", fg="black", relief=RAISED)

#positioning labels, buttons, and entry
username_label.grid(row=0, column= 1, sticky="W", pady="1", ipady="1", ipadx="1")
username_entry.grid(row=1, column=1)

first_label.grid(row=2, column=1, sticky="W", pady="1", ipady="1", ipadx="1")
first_entry.grid(row=3, column=1)

last_label.grid(row=4, column=1, sticky="W", pady="1", ipady="1", ipadx="1")
last_entry.grid(row=5, column=1)

email_label.grid(row=6, column=1, sticky="W", pady="1", ipady="1", ipadx="1")
email_entry.grid(row=7, column=1)

password_label.grid(row=8, column=1, sticky="W", pady="1", ipady="1", ipadx="1")
password_entry.grid(row=9, column=1)

log_btn.grid(row=10, column=2, sticky="W", pady="1", ipady="1", ipadx="1")
create_btn.grid(row=10, column=3, sticky="W", pady="1", ipady="1", ipadx="1")
clear_btn.grid(row=10, column=4, sticky="W", pady="1", ipady="1", ipadx="1")


root.mainloop()
