dan = int(input ("Which dan? "))

if dan > 0 and dan < 10:
    for num in range (1, 10):
    # ans = (int(dan) * int(num))
    # print (str(dan), "*" ,str(num), "=", ans)

        print ("{} * {} = {}".format(dan, num, dan*num))
