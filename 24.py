def inFunc():
    x = "Hello World"
    return x

def outFunc(x):
    print(x)
    print(type(x))

if __name__ == "__main__":
    x = inFunc()
    outFunc(x)