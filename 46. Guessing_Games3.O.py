Score = dict()
player1 = input("What is your name player1 - ")
player2 = input("What is your name player2 - ")
Score[player1] = 0
Score[player2] = 0
player1_list = list()
player2_list = list()
for k in range(1,5+1):
    CityNames1 = input("Pls type your fav city {} - ".format(player1))
    player1_list.append(CityNames1)

for m in range(1,5+1):
    CityGuess2 = input("Pls type the city name you think - ")
    if CityGuess2 in player1_list:
        Score[player2] = Score[player2] + 1

for k in range(1,5+1):
    CityNames2 = input("Pls type your fav city {} - ".format(player2))
    player2_list.append(CityNames2)

for m in range(1,5+1):
    CityGuess1 = input("Pls type the city name you think - ")
    if CityGuess1 in player2_list:
        Score[player1] = Score[player1] + 1

if (Score[player1] > Score[player2]):
    print("{} is the winner".format(player1))
    
elif (Score[player2] == Score[player1]):
    print("This is a tie")
    
else:
    print("{} is the winner".format(player2))
print(player1_list, player2_list)

print(Score[player1], Score[player2])
