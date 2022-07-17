Price = {"Apple": 29, "Mango": 119, "Grapes": 79}
print("The following are avilable in this market ")
for k in Price:
    print("item = {} => price per kg = {}".format(k, Price[k]))
num = int(input("How many items do you want to add, max: 3 - "))
Cart = dict()
for n in range(1,num+1):
    Item = input("What is the the item - ")
    Quantity = int(input("How many kg's you want to add, NO GRAMS - "))
    Cart[Item] = Quantity

print(Cart)

TotalAmt = 0   
for m in Cart:
    TotalAmt = TotalAmt + (Cart[m] * Price[m])
print("This is your bill - {}".format(TotalAmt))

    
    
