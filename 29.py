def inFun():
    x = range(6)
    return x

def outFunc(x):
    print(x)
    print(type(x))

if __name__ == "__main__":
    x = inFun()
    outFunc(x)