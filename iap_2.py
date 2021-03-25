# *args and **kwargs in python explained

def function_1(*args):
    print(type(args))
    if (len(args) ==3):
        print("The name of the student is",args[0], "and age is", args[1], "roleno is", args[2])
    else:
        print("The name of the student is",args[0], "and age is", args[1])

# lis = ["Udoy", 22, 4422]
# function_1("Udoy", 17)
# function_1(*lis)

#--------------

def marks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

marklist = {"udoy":100, "Harry":54, "Karan":67, "Rohan":98, "Fariha":89, "Maryam":78, "Mitu":92}
marks(**marklist)

#------------

def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)

marklist = {"udoy":100, "Harry":54, "Karan":67, "Rohan":98, "Fariha":89, "Maryam":78, "Mitu":92}
lis = ["Udoy", 22, 4422]

master("normal args", *lis, **marklist)