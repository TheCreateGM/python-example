# input function
def InFunc():
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"
    return myvar, my_var, _my_var, myVar, MYVAR, myvar2

# output function
def OutFunc(myvar, my_var, _my_var, myVar, MYVAR, myvar2):
    print(f"{myvar} {my_var} {_my_var} {myVar} {MYVAR} {myvar2}")

# main function
if __name__ == "__main__":
    myvar, my_var, _my_var, myVar, MYVAR, myvar2 = InFunc()
    OutFunc(myvar, my_var, _my_var, myVar, MYVAR, myvar2)