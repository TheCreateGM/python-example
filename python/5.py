# input values
def InVal():
    x = 5
    y = "Hello"
    z = "World"
    return x, y, z

# output values
def OutVal(x, y, z):
    print(x)
    print(f"{y}, {z}!")

# main function
if __name__ == "__main__":
    x, y, z = InVal()
    OutVal(x, y, z)