def inFunc():
    x = 20.5
    y = 1j
    return x, y

def outFunc(x, y):
    print(x)
    print(type(x))
    print(y)
    print(type(y))

if __name__ == "__main__":
    x, y = inFunc()
    outFunc(x, y)