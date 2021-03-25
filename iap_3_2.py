try:
    print("I will try this code and will throw exception if tehre is any problem * ")
except Exception as e:
    print("I will run only if try is block fails ** ")
else:
    print("I will run only if there is no exception. Use this to run code which should only excute if there is no exception *** ")
finally:
    print("Thsi will be printed in every case **** ")
