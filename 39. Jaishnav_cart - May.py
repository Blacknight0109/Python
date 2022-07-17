cart = list()
name = input("Hi pls type your name - ")
number = int(input("How many items do you want to add? - "))
for k in range(1,number + 1):
    item = input("Pls type your item - ")
    cart.append(item)

print ("{} These are your items".format(cart))
n = input("Do want to remove any item? if yes then pls type yes, if no pls type no - ")
if (n == "yes"):
    f = input("What item/items do you want to remove? - ")
    cart.remove(f)

print ("ok {}, these/this is your final order {}".format(name,cart))    
    



    
