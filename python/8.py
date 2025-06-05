# input function
def InFun():
    x = str(3)
    y = int(3)
    z = float(3)
    return x, y, z

# output function
def OutFun(x, y, z):
    print(x)
    print(y)
    print(z)

# main function
if __name__ == "__main__":
    x, y, z = InFun()
    OutFun(x, y, z)