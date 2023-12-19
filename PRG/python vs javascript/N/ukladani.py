with open("H:\\WET\\PRG\\python vs javascript\\N\\data.txt", "r") as file:
    print(file.read())

#file = open("H:\\WET\\PRG\\python vs javascript\\N\\data.txt", "r") #read
#file.close()

with open("H:\\WET\\PRG\\python vs javascript\\N\\data.txt", "w") as file:
    text = "Bye bye"
    file.write(text)

with open("H:\\WET\\PRG\\python vs javascript\\N\\data.txt", "a") as file: #apend
    text = "\nBye bye"
    file.write(text)