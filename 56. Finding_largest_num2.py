Num_list = list()
for k in range(1,4+1):
    Num_input = int(input("Pls type the num {} - ".format(k)))
    Num_list.append(Num_input)
Min_Num = 1000000
for n in Num_list:
    if (Min_Num > n):
        Min_Num = n
print(Min_Num)
