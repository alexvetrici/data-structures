class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def show(self):
        return self.stack

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]