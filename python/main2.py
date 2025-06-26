def inFunc():
    a = input("Enter input text: ")
    return a

def outFunc(a):
    print(a[::-1])

if __name__ == "__main__":
    a = inFunc()
    outFunc(a)