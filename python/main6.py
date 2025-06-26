class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"push({item})")

    def pop(self):
        if not self.is_empty():
            popped = self.items.pop()
            print(f"pop() -> {popped}")
        else:
            print("pop() -> Stack is empty")

    def peek(self):
        if not self.is_empty():
            print(f"peek() -> {self.items[-1]}")
        else:
            print("peek() -> Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

def inFunc():
    return ["push", "push", "peek", "pop", "peek", "empty"]

def outFunc(ops):
    s = Stack()
    for op in ops:
        if op == "push":
            s.push(1)
        elif op == "pop":
            s.pop()
        elif op == "peek":
            s.peek()
        elif op == "empty":
            print(f"empty() -> {s.is_empty()}")

if __name__ == "__main__":
    operations = inFunc()
    outFunc(operations)
