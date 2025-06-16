def colItem():
    x = ("apple", "banana", "cherry")
    return x

def inFunc(x):
    a = x[0]
    b = x[1]
    c = x[2]
    return a, b, c

def outFunc1(a, b, c):
    print(a, b, c)

def outFunc2(x):
    print(type(x))

if __name__ == "__main__":
    x = colItem()
    a, b, c = inFunc(x)
    outFunc1(a, b, c)
    outFunc2(x)