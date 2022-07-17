Marks = dict()
for k in range(1,2+1):
    Name = input("Pls type your name - ")
    Score = int(input("Pls type your marks - "))
    Marks[Name] = Score
print(Marks)
MaxMarks = -1
for n in Marks:
    if Marks[n] > MaxMarks:
        MaxMarks = Marks[n]
        Highest_scorer = n
print("This kid got the highest marks in the class {}".format(Highest_scorer))
    
