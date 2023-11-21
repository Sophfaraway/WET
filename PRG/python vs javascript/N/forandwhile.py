for x in range(5):
  print(x)

seznam = ["hrusky", "jablka", "jahody", "meloun"]

for jidlo in seznam:
  print(jidlo, end="...")  #to add something else after items instead of enter

print()  #so the next print will be on a new line

slovo = "slovo"
print(slovo[0]
      )  #[0] - number in brackets is the number of the letter in the word

for pismeno in slovo:
  print(pismeno)

print(seznam[0]
      [0])  #first [] is the word in the list, 2nd [] is the letter in the word

for i, polozka in enumerate(
    seznam):  #counting the numbers of the items in the list
  print(i + 1, polozka)  #starts counting from 1 not 0

# while True:
# continue - to skip over the iteration
#break - to stop a cycle