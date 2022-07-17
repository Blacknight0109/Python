def addition(N1,N2):
    result = N1 + N2
    print("The answer of your addition is {}".format(result))

def subtraction(N1,N2):
    result = N1 - N2
    print("The answer of your subtraction is {}".format(result))

def multiplication(N1,N2):
    result = N1 * N2
    print("The answer of your multiplication is {}".format(result))

def division(N1,N2):
    result = N1 / N2
    print("The answer of your division is {}".format(result))

while True:
    Calculator_option = input("Hi, what do u want to do \n addition = + \n subtraction = - \n multiplatcion = * \n division = / \n or press Q to quit \n")
    if (Calculator_option == "Q" or Calculator_option == "q"):
        break
    Num1 = int(input("Type your first number - "))
    Num2 = int(input("Type your second number - "))
    if(Calculator_option == "+"):
        addition(Num1,Num2)
    elif(Calculator_option == "*"):
        multiplication(Num1,Num2)
    elif (Calculator_option == "/"):
        division(Num1,Num2)
    elif(Calculator_option == "-"):
        subtraction(Num1,Num2)    

