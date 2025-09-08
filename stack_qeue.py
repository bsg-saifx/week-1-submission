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


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,val):
        self.queue.append(val)
    
    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.is_empty():
            print("Empty Queue")
        else:
            item = self.queue.popleft()
        return item

    def front(self):
        if self.is_empty():
            print("Empty Queue")
        else:
            return self.queue[0]
    def rear(self):
         if self.is_empty():
            print("Empty Queue")
         else:
            return self.queue[-1]
    def display(self):
        return list(self.queue)

print("Queue")
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
print(q.display())
print(q.front())
print(q.rear())
q.dequeue()
print(q.display())

print("Stack")
s = Stack()
s.push(10)
s.push(20)
print(s.display())
print(s.pop())
print(s.display())
