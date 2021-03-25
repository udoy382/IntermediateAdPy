# List Comprehension, Dictionary Comprehension, and Generator Comprehension

'''

List Comprehension
Dictionary Comprehension
Set Comprehension
Generator Comprehension

'''

list_1 = [1, 2, 5, 4, 8, 5, 3, 6, 9, 76, 56, 3, 54, 24, 24, 75, 86, 356, 35, 75]
divide_by_3 = []
for item in list_1:
    if item%3==0:
        divide_by_3.append(item)
print("Without using list Comprehension:", divide_by_3)

#       List Comprehension
print("Using list Comprehension: ", [item for item in list_1 if item%3==0])

#       Dictionary Comprehension
dict1 = {'a':45, 'b':65, 'A':5}
print({k.lower():dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

#       Set Comprehension
squared = {x**2 for x in [1, 3, 5, 2, 4, 3, 4, 4, 3, 4, 3, 2, 6, 5, 4, 3,2]}
print(squared)

#       Generator Comprehension
gen = (i for i in range(56) if i%3==0)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for item in gen:
    print(item)