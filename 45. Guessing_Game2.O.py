Score = dict()
Score["Deepanshu"] = 0
Score["Jaishnav"] = 0
Deepanshu = list()
Jaishnav = list()
for k in range(1,5+1):
    CityNamesJ = input("Pls type your fav city Jaishnav - ")
    Jaishnav.append(CityNamesJ)

for m in range(1,5+1):
    CityGuessD = input("Pls type the city name you think - ")
    if CityGuessD in Jaishnav:
        Score["Deepanshu"] = Score["Deepanshu"] + 1

for k in range(1,5+1):
    CityNamesD = input("Pls type your fav city Deepanshu - ")
    Deepanshu.append(CityNamesD)

for m in range(1,5+1):
    CityGuessJ = input("Pls type the city name you think - ")
    if CityGuessJ in Deepanshu:
        Score["Jaishnav"] = Score["Jaishnav"] + 1

if (Score["Deepanshu"] > Score["Jaishnav"]):
    print("Deepanshu is the winner")
    
elif (Score["Deepanshu"] == Score["Jaishnav"]):
    print("This is a tie")
    
else:
    print("Jaishnav is the winner")

print(Score["Deepanshu"], Score["Jaishnav"])
