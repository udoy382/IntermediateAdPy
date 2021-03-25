# Map, Filter and Reduce in Python

# map (function_to_apply, list of inputs)

'''
def square(n):
    return n**2

h1 = [1, 2, 4, 5, 7]

# sq = []

# for item in h1:
#     sq.append(item**2)
# print(sq)
sq = list(map(square, h1))
print(sq)
'''

#-----------------

'''
def greater_then_2(n):
    if n>2:
        return True
    else:
        return False

h1 = [1, 2, 4, 5, 6, 7, 3, -4, 6 ,-5]
greater_th_2 = list(filter(greater_then_2, h1))
print(greater_th_2)
'''

#------------------

'''
from functools import reduce

def sum_num(a, b):
    return a+b

li1 = reduce(sum_num, [1, 2, 3, 4])
print(li1)
'''