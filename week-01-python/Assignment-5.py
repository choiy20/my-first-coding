
def gugudan():
    try:
        dan = int(input("Enter a number between 2 and 9: "))
        if 1 < dan < 10:
            for num in range(1, 10):
                print("{} * {} = {}".format(dan, num, dan*num))
        else:
            print("Please enter a number between 2 and 9 only.")
            gugudan()  #다시 try부터 시작

    except ValueError:
        print("Please enter number only.")
        gugudan()   #재귀함수
    except:
        print ("Error. Please try agian.")
        gugudan()
gugudan()
