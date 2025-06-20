def inFunc():
    x = str(input("Enter text input: "))
    return x

def outFunc(x):
    print("\n" + x)
    print(type(x))

if __name__ == "__main__":
    x = inFunc()
    outFunc(x)
