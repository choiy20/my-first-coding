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



# print (brunch_article.source) # 새로 추가한 변수 확인
# print (brunch_article.view_count)
# brunch_article.read()
# print(brunch_article.view_count)



# person = People(name, age, gender)
#
# print (person.name, person.age, person.gender, person.title)
