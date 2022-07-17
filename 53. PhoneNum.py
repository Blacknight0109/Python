phone_num = list()
num = int(input("How many users are there? - "))
for n in range(1,num+1):
    phone_num2 = input("What's your phone num - ")
    phone_num.append(phone_num2)

valid_num_count = 0
invalid_num_count = 0
for k in range(0,num):
    if (len(phone_num[k]) == 10 and phone_num[k].isdigit()):
        print("this is a valid num")
    else:
        print("this is not a valid num")
