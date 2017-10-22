# restaurant = str(input("Please choose one from Korean, Chinese or Japanese: "))
#
#
# import random
#
# if restaurant in ["Korean".lower(), "Korea".lower()]:
#     korean = ["K1", "K2", "K3", "K4", "K5"]
#     print (random.choice(korean))
#
# elif restaurant in ["Chinese".lower(), "China".lower()]:
#     chinese = ["C1", "C2", "C3", "C4", "C5"]
#     print (random.choice(chinese))
#
# elif restaurant in ["Japanese".lower(), "Japan".lower()]:
#     japanese = ["J1", "J2", "J3", "J4", "J5"]
#     print (random.choice(japanese))
#
# else:
#     print ("Not valid. Please choose one from Korean, Chinese or Japanese")

###해답
import random

Korean_Food = ("Kimchijjigae", "Bibimbab", "Guksu")
Chinese_Food = ("Jjajangmyeon", "Tangsuyuk", "Jjambbong")
Japanese_Food = ("Ramen", "Donkatsu", "Donburi")

user_choice = input("Choose from Korean, Chinese and Japanese: ")

if user_choice == "Korean" or "Korean".lower():
    choice_result = random.choice(Korean_Food)
elif user_choice == "Chinese" or "Chinese".lower():
    choice_result = random.choice(Chinese_Food)
elif user_choice == "Japanese" or "Japanese".lower():
    choice_result = random.choice(Japanese_Food)
else:
    print("Please choose from Korean, Chinese and Japanese only.")

if choice_result:
    print ("{} is selected from {} food.".format(choice_result, user_choice))
