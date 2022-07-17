num_list = list()
number = int(input("How many numbers do you want to add? - "))
for n in range(1, number + 1):
    f = int(input("your number - "))
    num_list.append(f)

for item in num_list:
    if (item % 2 == 0):
        print ("Number is even {}".format(item))

    else:
        print("Number is odd {}".format(item))
    
