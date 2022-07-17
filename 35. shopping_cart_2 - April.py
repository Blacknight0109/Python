cart = list()
name = input("Hi! pls type your name ")
number = int(input("How much items you want to add "))
for n in range(1,number + 1):
    item = input("Pls type your item ")
    cart.append(item)

print ("{} these are your items in the list".format(cart))

k = input("Do you want to remove any item?. press y for yes and n for no ")
if(k == "y"):
    #h = int(input("how many items do u want to remove "))
    b = input("Pls tell what item do u want to remove ")
    cart.remove(b)
print ("Hi {} your Final order {}".format(name,cart))


