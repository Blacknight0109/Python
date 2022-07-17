Num_list = list()
def JaishnavMax(JList):
    max_num = 0
    for n in JList:
        if(max_num < n):
            max_num = n
    print("The largest number is {}".format(max_num))

for k in range(1,4+1):
    Num = int(input("Pls type the num - "))
    Num_list.append(Num)

JaishnavMax(Num_list)
    
