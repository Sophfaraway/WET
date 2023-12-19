import csv

# path = "H:\\WET\\PRG\\python vs javascript\\N\\data.csv"
# with open(path, "r") as f:
#     reader = csv.reader(f, delimiter=";")
#     for x in reader:
#         print(x)

path = "H:\\WET\\PRG\\python vs javascript\\N\\data.csv"
with open(path, "a", newline="") as f:
    name = input("Enter name: " )
    amount = int(input("Enter amount: " ))
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["hokus","pokus"])
    writer.writerow([name, amount])