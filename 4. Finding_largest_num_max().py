num_list = list()
Num_input = int(input("Pls type how many times you want to add - "))
for k in range(1,Num_input+1):
    Num = int(input("What is the num - "))
    num_list.append(Num)
print("This is the largest num {}".format(max(num_list)))
