num = list()
people = int(input("how many users are there - "))
for n in range(1,people+1):
    num_input = int(input("What is the num "))
    num.append(num_input)

valid_num = 0
invalid_num = 0
for k in num:
    if(k > 10 and k%2 == 0):
        print("This is a valid num {}".format(k))
        valid_num = valid_num + 1
    else:
        print ("this is a invalid num {}".format(k))
        invalid_num = invalid_num + 1
        
print("There are these many valid num {} and these many invalid num {}".format(valid_num,invalid_num))
