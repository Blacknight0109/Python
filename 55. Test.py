names = input("Hi! What is your name? - ")
email = input("Pls type your email - ")
names.count()
if(len(names) <= 10 and names.isalpha() and email.count('@')==1 and email.endswith('.com')):
print ("this is a valid name")
    print ("this is a valid email")
else:
    print ("this is not a valid name")
    print ("this is not a valid email id")

cart = list()
print ("Proceding...")
things_num = int(input("How many things do u want to add? - "))
for k in range(1,things_num + 1):
    things = input("Type the item you want - ")
    cart.append(k)
    print ("{} these are your items".format(k))
    reamove = input("Do you want to reamove anything? - ")
    if (ye == "yes"):
        f = input("What item/items do u want to remove? - ")
        cart.reamove(f)
        print("{} These are your items".format(things))
else:
    print ("There is some mistake in your email or your name! pls try again later")
    

            
