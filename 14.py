# input function
def InFunc():
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    return x, y, z

# output function
def OutFunc(x, y, z):
    print(x)
    print(y)
    print(z)

# main function
if __name__ == "__main__":
    x, y, z = InFunc()
    OutFunc(x, y, z)