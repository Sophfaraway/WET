import random
import tkinter as tk


names = ["Sophia", "Monika", "Julie", "Evžen", "Egon", "Marvin", "Ctirad", "Milan", "Jan", "Julius", "Patricius"]
last_name = ["Peble","Notme", "Garden", "Marry", "Halo"]
name = ""
surname = ""

def random_name():
    name = random.choice(names)
    surname = random.choice(last_name)
    r_name.config(text = name + " " + surname + " k tabuli!")

root = tk.Tk()
root.title("Name generator")

label = tk.Label(root, text="Your random name is:")
label.pack(pady=10)

button = tk.Button(root, text="press", command= random_name)
button.pack(pady=10)

r_name = tk.Label(root, text= name + " " + surname + " k tabuli!")
r_name.pack(pady=10)

root.mainloop()
