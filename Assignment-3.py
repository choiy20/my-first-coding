player = str(input("Rock, Paper, Scissors?: "))

#컴퓨터 랜덤
import random

computer= random.randint(1,3)
if (computer == 1):
    computer = "rock"
    print ("Rock")
elif (computer == 2):
    computer = "paper"
    print ("Paper")
elif (computer == 3):
    computer = "scissors"
    print ("Scissors")

#결과
if (player.lower() == computer):
    print("Draw! Please try again.")

elif (player.lower() == "rock"):
    if (computer == "paper"):
        print ("You lost!")
    else:
        print("You won!")

elif (player.lower() == "paper"):
    if (computer == "rock"):
        print ("You won!")
    else:
        print("You lost!")

elif (player.lower() == "scissors"):
    if (computer == "rock"):
        print ("You lost!")
    else:
        print ("You won!")
        
else:
    print ("Not valid. Please choose one from Rock, Paper or Scissors.")
