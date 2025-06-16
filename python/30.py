def colItem():
    x = {"name" : "John", "age" : 36}
    return x

def inFunc(x):
    a = x["name"]
    b = x["age"]
    return a, b

def outFunc1(a, b):
    print(a, b)

def outFunc2(x):
    print(type(x))

if __name__ == "__main__":
    x = colItem()
    a, b = inFunc(x)
    outFunc1(a, b)
    outFunc2(x)