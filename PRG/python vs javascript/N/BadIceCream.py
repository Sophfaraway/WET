import csv
import sys


def main():
    BadIceCream = {}

    load_data(BadIceCream)
    print("Welcome muhihahihahaaa")
    print("Choose option: ")
    print("To check all flavors choose 1")
    print("To check one flavor  choose 2")
    print("To add a point choose 3")
    print("To remove one flavor  choose 4")
    print("To see the flavor with most points choose 5")
    print("To add a flavor  choose 6")
    print("Press 7 to exit")

    while True:
        try:
            chosen_option = int(input())
            break
        except ValueError:
            print("Wrong input... did you input a number?")

    match chosen_option:
        case 1:
            allFlavours(BadIceCream)
        case 2:
            pointsSingleFlavour(BadIceCream)
        case 3:
            addPoint(BadIceCream)
        case 4:
            takePoint(BadIceCream)
        case 5:
            mostPoints(BadIceCream)
        case 6:
            addFlavour(BadIceCream)
        case 7:
            print("Bye bye")
            sys.exit()
        case _:
            print("Please choose one of the options")

    save_data(BadIceCream)


def pointsSingleFlavour(BadIceCream):
    flavour = input("Check points for flavour: ").capitalize()
    if flavour in BadIceCream:
        print(flavour, BadIceCream[flavour])


def allFlavours(BadIceCream):
    for i in BadIceCream:
        print(i, BadIceCream[i])


def addPoint(BadIceCream):
    add = input("Who do you want to add a point to?: ").capitalize()
    BadIceCream[add] += 1
    print(add, BadIceCream[add])


def takePoint(BadIceCream):
    take = input("Who do you want to take a point from?: ").capitalize()
    BadIceCream[take] -= 1
    print(take, BadIceCream[take])


def addFlavour(BadIceCream):
    nextFlavour = input("Add flavour: ").capitalize()
    BadIceCream[nextFlavour] = 1
    print(nextFlavour, BadIceCream[nextFlavour])


def mostPoints(BadIceCream):
    leading = max(BadIceCream, key=BadIceCream.get)
    print("And the one with the most points is \x1B[3m..drumroll...\x1B[0m : ")
    print(leading, BadIceCream[leading])


def save_data(BadIceCream):
    with open(
        "H:\\WET\\PRG\\python vs javascript\\N\\cat.csv", "w", newline=""
    ) as file:
        writer = csv.writer(file, delimiter=";")
        for flavor, points in BadIceCream.items():
            writer.writerow([flavor, points])


def load_data(BadIceCream):
    with open("H:\\WET\\PRG\\python vs javascript\\N\\cat.csv", "r") as file:
        reader = csv.reader(file, delimiter=";")
        for addKeys in reader:
            BadIceCream[addKeys[0]] = int(addKeys[1])
    print(BadIceCream)


if __name__ == "__main__":
    main()
