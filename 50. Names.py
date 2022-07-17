names = list()
num = int(input("How many users are there - "))
for n in range(1,num+1):
    names2 = input("What's you name - ")
    names.append(names2)

valid_name = 0
invalid_name = 0
for k in range(0,num):
    if (len(names[k]) <= 8 and names[k].isalpha()):
        print("this is a valid name")
        valid_name = valid_name + 1
    else:
        print("this is not a valid name")
        invalid_name = invalid_name + 1

print("There are {} valid names and {} invalid names".format(valid_name,invalid_name))

  
