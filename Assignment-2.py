class People:

    def __init__(self, name, age, gender, title):
        self.name = name
        self.age = age
        self.gender = gender
        self.title = title

name = input("What is your name? ")
age = input("What is your age? ")
gender = input("What is your gender? ")

class Smarterme(People):
    title = input("What is your title? ")
    smartermeteam = People(name, age, gender, title)

print (smartermeteam.name, smartermeteam.age, smartermeteam.gender, smartermeteam.title)
