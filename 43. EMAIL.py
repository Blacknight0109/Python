email = list()
num = int(input("How many users are there - "))
for n in range(1,num + 1):
    email_id = input("What's your email id - ")
    email.append(email_id)
valid_count = 0
invalid_count = 0
for k in range(0,num):
    if (email[k].count("@")==1 and email[k].endswith(".com")):
        #print(" this is a valid email")
        valid_count = valid_count+1
    else:
        print("this is not a valid email")
        invalid_count = invalid_count+1
print ("there are {} invalid email and {} valid email".format(invalid_count,valid_count))
    

