user1 = input("type your name      ")
n = int(input("type your number    "))
if (n<6):
    print ("Congrats {}".format(user1))
elif (n == 6):
    print ("You are close {}".format(user1))
else:
    print ("Better luck next time {}".format(user1))
