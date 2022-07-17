#Assignment No 01, Date 13/June/2022
#Largest Number in the list 
lst = list()
while True:
    Input = input("Hi! these r the instructions for u to do now \n 1st type the number \n 2nd after writing your num type q to quit ")
    if (Input == "Q" or Input == "q"):
        break
    Num = int(Input)
    lst.append(Num)
print("This the largest num {}".format(max(lst)))


    


        


