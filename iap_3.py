# try:
#     open("this.txt")
# except Exception as e:
#     print(e)

# # open("that.txt")
# print("Program zinda hai")

#-------------

try:
    file = open("that.txt", "r")
except EOFError as e:
    print("eof error")
except IOError as e:
    print("We can handle this error")

finally:
    print("This will be printed irrespetive of the exception occurrence")
