num_list = list()
number = int(input("How much people's marks do you want to add? - "))
for n in range(1, number + 1):
    k = int(input("What is the marks "))
    num_list.append(k)
count = 0
fail_count = 0
for item in num_list:
    if (item > 40):
        count = count + 1
    else:
        fail_count = fail_count + 1

print("These are the num of people who have failed {}".format(fail_count))

print("These are the num of people who have passed {}".format(count))

    

