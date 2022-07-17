#following is the number of fav fruits a user has
number_fav_fruits = int(input("Plese enter how may favourite fruits you have?"))
#following is an emty list where we will apend user's fav fruits
list_fav_fruits = []

# Following for loop is to create the list of the fav fruits of the user
for num in range(1,number_fav_fruits+1):
    #first ask fav fruit of user one by one in loop and save it
    #in a temporary variable fav_fruit which we will pass as input to append
    
    fav_fruit = input("please enter your fav fruit")
    #append the item to list
    list_fav_fruits.append(fav_fruit)

#Write the loop tio check each item in list_fav_fruits one by one

apple_found = 0
for fruit in list_fav_fruits:
    if(fruit == "apple"):
        apple_found = 1
        break

if(apple_found == 0):
    print("no apple found")
else:
    print("apple found")
