# Format Function In Python Explained

users = ["Rohan das", "Shubham", "Skil f", "Fariha", "Maryam"]

computer = ["Respberry pi", "Android", "I phone", "Mi", "Snmsung"]

# for i in range(0, len(users)):
#     print("Computer used by ", users[i], " is ", computer[i])


for i in range(0, len(users)):
    template = "Computer used by {1} is {0}"
    print(template.format(users[i], computer[i]))