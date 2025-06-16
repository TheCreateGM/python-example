# input function
def InFun():
    x = 5
    y = "John"
    return x, y

# output function
def OutFun(x, y):
    print(str(type(x)) + " " + str(x))
    print(str(type(y)) + " " + str(y))

# main function
if __name__ == "__main__":
    x, y = InFun()
    OutFun(x, y)