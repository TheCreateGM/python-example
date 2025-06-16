def inFunc():
    x = bytearray(5)
    return(x)

def outFunc(x):
    print(x)
    print(type(x))

if __name__ == "__main__":
    x = inFunc()
    outFunc(x)