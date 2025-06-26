def inmethod():
    pi = 3.14159
    r = float(input())
    return pi, r

def proformula(pi, r):
    circle_area = pi * r * r
    return circle_area

def outmethod(circle_area):
    print(f"{circle_area:.2f}")

if __name__ == "__main__":
    pi, r = inmethod()
    circle_area = proformula(pi, r)
    outmethod(circle_area)