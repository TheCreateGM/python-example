# input function
def InFun():
    x = "Python"
    y = "is"
    z = "python"
    return x, y, z

# output function
def OutFun(x, y, z):
    print(x, y, z)

# main function
if __name__ == "__main__":
    x, y, z = InFun()
    OutFun(x, y, z)