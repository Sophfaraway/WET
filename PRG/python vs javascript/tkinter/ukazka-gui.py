import tkinter as tk

root = tk.Tk()
root.title("Great GUI")

root.geometry("400x300")

label = tk.Label(root, text="very creative text insert")
label.pack()


def on_click():
    label.config(text="Something happened")


button = tk.Button(root, text="Click me!", command=on_click)
button.pack()

root.mainloop()
