Num_list = list()
for k in range(1,4+1):
    Num = int(input("Pls type the num - "))
    Num_list.append(Num)
Max_Num = 0
for n in Num_list:
    if (Max_Num < n):
        Max_Num = n
print(Max_Num)
