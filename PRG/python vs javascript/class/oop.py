class Student:
    def __init__(self, name, school, color):
        self.name = name
        self.school = school
        self.fav_color = color

    def speak(self, greeting):
        print(f"{greeting}My favourite color is {self.fav_color}")


class Zak(Student):
    def __init__(self, name, school, color):
        super().__init__(name, school, color)


hvezdon = Student("Hvězdoň", "Třebešín", "yellow")

print(hvezdon.fav_color)
hvezdon.speak("Hewwo ")

rizek = Student("Řízek", "Úžlabina", "blue")
rizek.speak("Od slova řízek ")

ida = Zak("Ida", "Jakutská", "růžová")
ida.speak("Dobrý den ")
