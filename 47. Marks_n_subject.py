NumSubjects = int(input("How many subjects are there? - "))
MarksSubject = dict()
for k in range(1,NumSubjects + 1):
    Subject = input("What are the subjects - ")
    Marks = int(input("What are the marks - "))
    MarksSubject[Subject] = Marks
SubjectsSelection = input("What suject's marks do you want \n If you want to print all the subjects marks then type 'all' - ")
if (SubjectsSelection == "All" or SubjectsSelection == "all" or SubjectsSelection == "ALL"):
    print("The marks of your subjects are {}".format(MarksSubject))
else:
    print ("This is the marks for the subject you have choosed {}".format(MarksSubject[SubjectsSelection]))
