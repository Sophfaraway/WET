import random
import tkinter as tk
import csv

with open('numbers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='unix')

pick_grade = ""
average = ""
aver_mark = []

def random_grade():
    input_text = entry.get()
    if input_text == "Sophia":
        pick_grade = random.choices(znamky, weights=(40, 20, 20 ,20, 0), k=1)
        print(pick_grade[0])
        aver_mark.append(pick_grade[0])
        average = sum(aver_mark) / len(aver_mark)
        cislo.config(text = pick_grade)
        cislo2.config(text = average)
    else:
        pick_grade = random.choice(znamky)
        print(pick_grade)
        aver_mark.append(pick_grade)
        average = sum(aver_mark) / len(aver_mark)
        cislo.config(text = pick_grade)
        cislo2.config(text = average)

    if average > 4.3:
        cislo.config(fg="red")
    elif average < 1.5:
        cislo.config(fg="green")
    else:
        cislo.config(fg="black")

    

root = tk.Tk()
root.title("Grade generator")

label = tk.Label(root, text="Please enter name:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Submit", command=random_grade)
button.pack(pady=10)

cislo = tk.Label(root, text= pick_grade)
cislo.pack(pady=10)

cislo2 = tk.Label(root, text= average)
cislo2.pack(pady=10)

znamky = [1, 2, 3, 4, 5]

root.mainloop()


