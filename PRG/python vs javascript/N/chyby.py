import sys

def positive_negative(x):
    if x > 0 :
        print("The number is positive")
    elif x < 0:
        print("The number is negative")
    else:
        print("The number is 0")

while True:
    try:
        number = int(input("Input number: "))
        positive_negative(number)
    except KeyboardInterrupt:
        print("Program closed manually")
        sys.exit()
    except ValueError:
        print("Wrong input... did you input a number?")
    else:
        print("Code was executed correctly")
        break
    finally:
        print("Finally is always printed")

