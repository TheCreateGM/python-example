def inFunc():
    num = input("enter number: ").split()
    a, b, c = map(int, num)
    return a, b, c

def outFunc(a, b, c):
    large = max(a, b, c)
    return large

def display(large):
    print("large number is", large)

if __name__ == "__main__":
    a, b, c = inFunc()
    large = outFunc(a, b, c)
    display(large)