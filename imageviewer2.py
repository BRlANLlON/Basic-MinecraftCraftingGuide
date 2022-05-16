from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

root.title("bitch")
root.configure(bg="#6F430C")
root.geometry("500x500")

#icon
p1 = PhotoImage(file = "logo.png")
root.iconphoto(False, p1)

#frame 1
frame_1 = tk.Frame(root, bg="white", height = "350", width = "350")
frame_1.pack(side=tk.BOTTOM)
frame_1.place(relx=0.5, rely=0.5, anchor = (tk.CENTER))

#frame2
frame2 = tk.Frame(frame_1, width=100, height=20, bg="red")
frame2.pack(side = tk.BOTTOM)


#frame3
frame3_image = tk.Frame(frame_1, width=300, height=300, bg="yellow")
frame3_image.pack(side = tk.TOP)

def showimage():
    axe = Image.open("axe.png")
    axe.show()
    axe_label = Label(frame3_image)
    image_label.pack()
    
def browse():
    recipe = recipe_var.get()
    if recipe == "axe":
        command = showimage

   

#inside frame 2

#string variable
recipe_var = tk.StringVar()

#string entry with label
recipe_label = tk.Label(frame2, text = "Browse Recipe:", font=("open sans", 7, "bold"))
recipe_entry = tk.Entry(frame2, textvariable = recipe_var, font=("open sans", 10, "normal"))

#button with command
browse_btn = tk.Button(frame2, text = "Browse", font=("open sans", 7), command = browse)

#grid
recipe_label.grid(row=0, column=0, sticky="W", pady="2", ipady="1", ipadx="1")
recipe_entry.grid(row=0, column=2, sticky="N", pady="1", ipady="1", ipadx="1")
browse_btn.grid(row=0, column=3, sticky="E", pady="1", ipady="1", ipadx="1")

root.mainloop()
