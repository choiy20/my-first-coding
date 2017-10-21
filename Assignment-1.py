Restaurant = str(input ("Please choose one from Korean, Chinese or Japanese: "))


import random

if Restaurant in ["Korean", "korean", "kor", "Korea", "korea"]:
    Korean = ["K1", "K2", "K3", "K4", "K5"]
    print (random.choice(Korean))

elif Restaurant in ["Chinese", "chinese", "chi", "China", "china"]:
    Chinese = ["C1", "C2", "C3", "C4", "C5"]
    print (random.choice(Chinese))

elif Restaurant in ["Japanese", "japanese", "jap", "Janpan", "japan"]:
    Japanese = ["J1", "J2", "J3", "J4", "J5"]
    print (random.choice(Japanese))

else:
    print ("Not valid. Please choose one from Korean, Chinese or Japanese")
