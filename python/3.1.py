import sys

def DisIn():
    a = sys.version
    b = sys.thread_info
    c = sys.api_version
    return a, b, c

def DisOut(a, b, c):
    print(a)
    print(b)
    print(c)

if __name__ == "__main__":
    a, b, c = DisIn()
    DisOut(a, b, c)