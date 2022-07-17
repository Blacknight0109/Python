Box = ["Snake","Snake","Diomand","Snake"]
print("There are four boxes above, In one of those boxes there is a key, Now you need to find the key")
while True:
    BoxGuess = int(input("Type your guess - "))
    if (Box [BoxGuess - 1] == "Snake"):
        print("Try again")
    else:
        print("You won")
        break
