# input function
def InFun():
    a = 4
    A = "Sally"
    return a, A

# output function
def OutFun(a, A):
    print(a)
    print(A)

# main function
if __name__ == "__main__":
    a, A = InFun()
    OutFun(a, A)