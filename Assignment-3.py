# player = str(input("Rock, Paper, Scissors?: "))
#
# #컴퓨터 랜덤
# import random
#
# computer= random.randint(1,3)
# if (computer == 1):
#     computer = "rock"
#     print ("Rock")
# elif (computer == 2):
#     computer = "paper"
#     print ("Paper")
# elif (computer == 3):
#     computer = "scissors"
#     print ("Scissors")
#
# #결과
# if (player.lower() == computer):
#     print("Draw! Please try again.")
#
# elif (player.lower() == "rock"):
#     if (computer == "paper"):
#         print ("You lost!")
#     else:
#         print("You won!")
#
# elif (player.lower() == "paper"):
#     if (computer == "rock"):
#         print ("You won!")
#     else:
#         print("You lost!")
#
# elif (player.lower() == "scissors"):
#     if (computer == "rock"):
#         print ("You lost!")
#     else:
#         print ("You won!")
#
# else:
#     print ("Not valid. Please choose one from Rock, Paper or Scissors.")



##### 해답

import random

ROCK = "rock"
SCISSORS = "scissors"
PAPER = "paper"
RSP_LIST = (ROCK, SCISSORS, PAPER)

win_count = 0
lose_count = 0

while win_count <3 and lose_count <3:
    user_choice = input("{}, {}, {}: ".format(ROCK, SCISSORS, PAPER))

#2) 컴퓨터의 임의 선택
    computer_choice = random.choice(RSP_LIST)
    print (computer_choice)

#3) 3번 지거나 이기면 승패 확정
    if user_choice == computer_choice:
        print ("Draw!")

    elif ((user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == SCISSORS and computer_choice == PAPER)
        or (user_choice == PAPER and computer_choice == ROCK)):
        win_count = win_count + 1
        print ("You won!")

    else:
        lose_count = lose_count + 1
        print ("You lost!")

if win_count == 3:
    print ("You won the entire game!")

elif lose_count == 3:
    print ("You lost the entire game. Try again!")
