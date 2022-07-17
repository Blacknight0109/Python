Num_list = list()
def JaishnavMin(JList):
    Min_Num = 1000000000
    for n in JList:
        if (Min_Num > n):
            Min_Num = n
    print("The min num is {}".format(Min_Num))

for k in range(1,4+1):
    Num = int(input("Pls type the num - "))
    Num_list.append(Num)
JaishnavMin(Num_list)
