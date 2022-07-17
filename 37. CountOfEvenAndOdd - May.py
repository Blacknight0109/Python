num_list = list()
number = int(input("How many people are going to give their numbers? - "))
for n in range(1,number + 1):
    k = int(input("What is the number person? - "))
    num_list.append(k)
even_count = 0
odd_count = 0
for answers in num_list:
    if (answers % 2):
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("These are the numbers which are even {}".format(even_count))
print("These are the numbers which are odd {}".format(odd_count))
