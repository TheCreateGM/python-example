# input function
def InFun():
    x = 5
    y = "John"
    return x, y

# output function
def OutFun(x, y):
    print(x, y)

# main function
if __name__ == "__main__":
    x, y = InFun()
    OutFun(x, y)