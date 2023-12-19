import random

cislo = random.randint(1, 10)

print(cislo)

mquestion = input("What\'s your question?\n")

magicball = random.randint(1, 6)

if magicball == 1:
  print("YAS")
elif magicball == 2:
  print("Yes")
elif magicball == 3:
  print("We shall never know")
elif magicball == 4:
  print("Maybe")
elif magicball == 5:
  print("Nah")
elif magicball == 6:
  print("No")
elif magicball == 7:
  print("Try again")

seznam = [
    "YAS", "Yes", "We shall never know", "Maybe", "Nah", "No", "Try again"]