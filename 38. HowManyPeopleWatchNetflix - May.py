num_list = list()
person_number = int(input("How many people are there?? - "))
for n in range(1, person_number + 1):
    k = input("Do you watch Netflix? y for yes and n for no - ")
    num_list.append(k)
yes_count = 0
no_count = 0
for answer in num_list:
    if (answer == "y"):
        yes_count = yes_count + 1
    else:
        no_count = no_count + 1
print("These many people told no {}".format(no_count))
print("These many people told yes {}".format(yes_count))
