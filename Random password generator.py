import random
from tkinter import * 

root = Tk()
root.title('Random Password Generator')
root.geometry('450x450')
root.config(bg="cyan")

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*_-+=.?<>'

characters = alpha + numbers + symbols

randompass=Label(root, text="Random password Generator", fg="red", font=('Arial', 15)).pack(padx=10)

label_characters = Label(root, text="Number of characters", font=('Arial', 13),bg="grey", fg="yellow",bd=3).pack(padx=10, pady=30)
character_length = Entry(root, font="Arial 13",bg="wheat")
character_length.pack(padx=10)

def generate_password():
    length = character_length.get()
    password = "".join(random.sample(characters, int(length)))
    label_password.config(text='Generated Password: ' + password,fg="maroon")

Button(root, text="Generate Password", command=generate_password, font=('Arial', 13),bg="grey",fg="yellow", bd=3).pack(padx=10, pady=60)
label_password = Label(root, font=('Arial', 13), bg="wheat")
label_password.pack()

root.mainloop()