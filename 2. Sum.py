#Assignment No 2, 14/Jun/2022
#Sum in the list
lst = list()
while True:
    Input_Num = input("Hi! \n Pls type the num \n Type quit once u r done - ")
    if (Input_Num == "Q" or Input_Num == "q"):
        break
    Num = int(Input_Num)
    lst.append(Num)
print("The answer is {}".format(sum(lst)))
