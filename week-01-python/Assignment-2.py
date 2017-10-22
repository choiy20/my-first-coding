# class People:
#
#     def __init__(self, name, age, gender, title):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.title = title
#
#
# name = input("What is your name? ")
# age = input("What is your age? ")
# gender = input("What is your gender? ")
#
# class Smarterme(People):
#     title = "Associate"
#     # title = input("What is your title? ")
#     smarterme = People(name, age, gender, title)
#
#     print (smarterme.name, smarterme.age, smarterme.gender, smarterme.title)


###해답
#1) 사람 클래스
class Person:
    # 이름, 나이, 성별
    # name, age, gender
    # 1-1) 새로 만들 때 입력
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#2) 직장 동료 클래스
# 상속
class Colleagues(Person):
    # 2-1) 기본 직급 대리
    # position = "대리"
    # 2-2) 새로 만들 때 입력
    def __init__(self, name, age, gender, position):
        super().__init__(name, age,gender) #super 사용해서 부모클래스 (Person)가 가지고 있는 함수를 호출.
        self.position = position

colleague = Colleagues("Kelly", 30, "Female", "Associate")
print (colleague.__dict__) #dict 형태로 보여주기
