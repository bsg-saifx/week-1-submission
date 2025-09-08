from collections import deque

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

q = Queue()

q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
print(q.display())
print(q.front())
print(q.rear())
q.dequeue()
print(q.display())
