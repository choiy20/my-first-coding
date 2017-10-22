restaurant = str(input("Please choose one from Korean, Chinese or Japanese: "))


import random

if restaurant in ["Korean", "Korean".lower(), "Korea", "Korea".lower()]:
    korean = ["K1", "K2", "K3", "K4", "K5"]
    print (random.choice(korean))

elif restaurant in ["Chinese", "Chinese".lower(), "China", "China".lower()]:
    chinese = ["C1", "C2", "C3", "C4", "C5"]
    print (random.choice(chinese))

elif restaurant in ["Japanese", "Japanese".lower(), "Janpan", "Japan".lower()]:
    japanese = ["J1", "J2", "J3", "J4", "J5"]
    print (random.choice(japanese))

else:
    print ("Not valid. Please choose one from Korean, Chinese or Japanese")
