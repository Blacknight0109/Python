City_names = list()
for k in range(1,5+1):
    user1 = input("Type your city name - ")
    City_names.append(user1)
ValidCityNames = 0
for m in range(1,5+1):
    user2 = input("Your guess - ")
    if (user2 in City_names):
        ValidCityNames == ValidCityNames + 1
if (ValidCityNames >= 3):
    print ("You win")
else:
    print("You lose")
