# lambda function in python

'''

Syntax:
lambda argument : manipulate(argument)

'''

# def add(a, b):
#     s = a+b
#     return s
# print(add(4, 6))

# add = lambda x, y:x+y
# print(add(4, 15))

#-----------

a = [(1, 2), (555, 34), (4, 5)]
a.sort(key=lambda x:x[1])
print(a)