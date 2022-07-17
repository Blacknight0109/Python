name_1 = input("Hi student 1 pls type your name - ")
student_1_age = int(input ("What's your age - "))
student_1_roll_num = int(input("what's your roll num - "))
student_1_marks = int(input("What's your marks - "))

name_2 = input("Hi student 2 pls type your name - ")
student_2_age = int(input ("What's your age - "))
student_2_roll_num = int(input("what's your roll num - "))
student_2_marks = int(input("What's your marks - "))

student1_details = dict()
student1_details ["name"] = name_1
student1_details  ["age"] = student_1_age
student1_details ["roll_num"] = student_1_roll_num
student1_details ["marks"] = student_1_marks

student2_details = dict()
student2_details ["name"] = name_2
student2_details  ["age"] = student_2_age
student2_details  ["roll_num"] = student_2_roll_num
student2_details  ["marks"] = student_2_marks

if (student1_details["marks"] > student2_details["marks"]):
    print("The student who got the highest marks is {} roll num {} age {}".format(student1_details["name"],student1_details["roll_num"],student1_details["age"]))

else:
    print("The student who got the highest marks is {} roll num {} age {}".format(student2_details["name"],student2_details["roll_num"],student2_details["age"]))



    
