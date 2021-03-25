'''

Iterable - 
Iterator - 
Iteration - 

'''

def gen(n):
    for i in range(n):
        yield i

# print(gen(1000))
# for i in gen(1000):
#     print(i)

ob1 = gen(4)
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))
# print(next(ob1))

#       Iterable

num = "udoy"
# for i in num:
#     print(i)

iter1 = iter(num)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1)) 