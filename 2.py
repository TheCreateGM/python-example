def DisIn():
    a = "Hello"
    b = "World!"
    return a, b

def DisOut(a, b):
    print(a + ", " + b)

if __name__ == "__main__":
    a,b = DisIn()
    DisOut(a, b)