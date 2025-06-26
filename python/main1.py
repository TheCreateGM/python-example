def inFunc():
    num = input("Enter number:")
    num = list(map(int, num.split()))
    return num

def calcFormula(num):
    even_num = list(filter(lambda x : x % 2 == 0, num))
    total = sum(even_num)

    print("Sum: ", total)

if __name__ == "__main__":
    num = inFunc()
    calcFormula(num)