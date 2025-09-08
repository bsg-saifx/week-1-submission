from collections import deque

class Stack:
    def __init__(self):
        self.stack= deque()

    def push(self,val):
        self.stack.append(val)

    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if self.is_empty():
            print("Empty stack")
        else:
            item = self.stack.pop()
            return item
    def top(self):
        if self.is_empty():
            print("Empty stack")
        else:
            return self.stack[-1]
    def display(self):
        return list(reversed(self.stack))

s = Stack()
s.push(10)
s.push(20)
print(s.display())
print(s.pop())
print(s.display())

