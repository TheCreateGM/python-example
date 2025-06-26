def inFunc():
    num = int(input("Enter number: "))
    return num

def outFunc(num):
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

if __name__ == "__main__":
    num = inFunc()
    outFunc(num)