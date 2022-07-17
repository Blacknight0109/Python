name = input("Pls type your full name (eg - Krishna Murthi) - ")
#print (name.capitalize())
#print (name)
num = input("What's your phone num - ")
#if (num.isdigit()):
    #print ("{} is a valid num".format(num))

#else:
    #print ("{} is not a valid num".format(num))

name2 = name.replace(' ','')

if (name2.isalpha()):
    print ("{} this is a valid name".format(name))

else:
    print("{} this is not a valid name".format(name))

if(len(num) == 10 and num.isdigit()):
	print("{} is a valid number".format(num)) 
else:
    print("{} is not a valid number".format(num))
    
email = input("pls type your emil id - ")
if (email.count("@")== 1 and email.endswith("gmail.com")):
    print("{} this is a valid email".format(email))

else:
    print("{} This is not a valid email".format(email))
