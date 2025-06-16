def colItem():
    x = frozenset({"apple", "banana", "cherry"})
    return x

def inFunc(x):
    x_l = list(x)
    a = x_l[0]
    b = x_l[1]
    c = x_l[2]
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