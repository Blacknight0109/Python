name = input("Hi! Pls type your name - ")
age = int(input("What's your age? - "))
roll_num = int(input("What's your roll num - "))
student_details = dict()
student_details["name"] = name
student_details["age"] = age
student_details["roll_num"] = roll_num
print ("The name of the student is {} his age is {} and his roll_num is {}".format(student_details["name"], student_details["age"],student_details["roll_num"]))

