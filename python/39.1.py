def inFunc():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return x, y

def calcFomula(x, y):
    total = x + y
    return total

def outFunc1(total):
    print(total)

def outFunc2(x, y):
    print(type(x))
    print(type(y))

if __name__ == "__main__":
    x, y = inFunc()
    total = calcFomula(x, y)
    outFunc1(total)
    outFunc2(x, y)