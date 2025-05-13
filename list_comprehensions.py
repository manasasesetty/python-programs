squares = [] # normal empty list
for i in range(1,11):   #create a list of squares of numbers from 1 to 10
    squares.append(i*i) # define what each loop iteration should do
print(squares)

print("______________________ \n ")

squares_1 = [i*i for i in range(1,11)] # list comprehension
print(squares_1)

print("______________________ \n ")

employee = [90,99,23,34,56,78,98,14,16]

experienced = list(filter(lambda x: x>50, employee)) # filter function

print(experienced)

print("______________________ \n ")

experienced_1 = [x for x in employee if x>50] # list comprehension
print(experienced_1)

print("______________________ \n ")

experienced_2 = [x if x>50 else "fresher" for x in employee] # list comprehension with if else

print(experienced_2)