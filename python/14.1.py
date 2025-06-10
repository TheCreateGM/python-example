# collection function
def ColFun():
    fruits = ["apple", "banana", "cherry"]
    return fruits

# input function
def InFun(fruits):
    x = fruits[0]
    y = fruits[1]
    z = fruits[2]
    return x, y, z

# output function
def OutFun(x, y, z):
    print(x)
    print(y)
    print(z)

# main function
if __name__ == "__main__":
    fruits = ColFun()
    x, y, z = InFun(fruits)
    OutFun(x, y, z)