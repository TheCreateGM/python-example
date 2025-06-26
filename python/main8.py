def colitem():
    arr = [1, 2, 3, 4, 5]
    return arr

def findsum(arr):
    total = 0
    for num in arr:
        total += num
    return total

def outprint(total):
    print("Sum:", total)

if __name__ == "__main__":
    arr = colitem()
    total = findsum(arr)
    outprint(total)