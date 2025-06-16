# input value
def InVal():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    return a, b

# Output value
def OutVal(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print("Error.")

# main function
if __name__ == "__main__":
    a, b = InVal()
    OutVal(a, b)