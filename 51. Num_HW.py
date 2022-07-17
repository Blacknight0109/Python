Num1 = list()
people = int(input("How many users are there - "))
for n in range(1,people+1):
    num2 = int(input("Pls type your num - "))
    Num1.append(num2)

invalid_num = 0
for k in Num1:
    if (k>= 100):
        invalid_num = 1
        break

if (invalid_num == 0):
    print("Invalid valid num not found")
else:
    print("Invalid num found")
