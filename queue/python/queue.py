# Queue implementation with double-ended queue (deque) method

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.popleft()

    def isEmpty(self):
        return len(self.queue) == 0

    def show(self):
        return self.queue

    def size(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]
