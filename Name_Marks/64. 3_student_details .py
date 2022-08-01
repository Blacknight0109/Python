FileName = input("Pls type the file name - ")
File = open(FileName ,"r")
StudentDict = dict()
for k in File:
    k = k.strip('\n')
    FileSplit = k.split(' ')
    print("{} has {} marks".format(FileSplit[0], FileSplit[2]))
    StudentDict[FileSplit[0]] = FileSplit[2]

Max_Num = 0
stud_name_max = ""
for n in StudentDict:
    if (Max_Num < int(StudentDict[n])):
        Max_Num = int(StudentDict[n])
        stud_name_max = n

print("The largest marks who got is {} the marks = {}".format(stud_name_max, StudentDict[stud_name_max]))
