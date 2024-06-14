import tkinter as tk
import random

root = tk.Tk()
root.title("Whac a mole")

score = 0
current_mole = None
moles = []


def choose_mole():
    global moles, current_mole
    current_mole = random.choice(moles)
    current_mole.config(bg="red")


def whac(event):
    global score, current_mole
    if event.widget == current_mole:
        print("Auch")
        global score
        score += 1
        score_label.config(text=f"Score: {score}")


def create_grid():
    for row in range(3):
        for col in range(3):
            mole = tk.Button(root, text="", width=12, height=5, bg="#1520A6")
            mole.bind("<Button-1>", whac)
            mole.grid(row=row, column=col)
            moles.append(mole)


score_label = tk.Label(root, text=f"Score: {score}")
score_label.grid(row=4, column=0)


create_grid()
choose_mole()
root.mainloop()
