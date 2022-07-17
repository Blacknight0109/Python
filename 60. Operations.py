operation = list()
initial_value = int(input("What is the initial value - "))
operation_count = int(input("How many operation are you going to add - "))
for K in range(1,operation_count+1):
    operation_value = input("What operation do u want to perform \n --x and x-- \n ++x and x++ ")
    operation.append(operation_value)
print(operation)
for choice in operation:
    if ("-" in choice):
        initial_value = initial_value - 1
    else:
        initial_value = initial_value + 1
print(initial_value)
