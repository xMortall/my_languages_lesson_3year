x = None
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("Something else went wrong")