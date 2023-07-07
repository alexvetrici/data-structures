# Queue implementation with double-ended queue (deque) method

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enQueue(self, data):
        self.queue.append(data)

    def deQueue(self):
        self.queue.popleft()

    def isEmpty(self):
        return len(self.queue) == 0

    def show(self):
        return self.queue

    def size(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]


# Queue implementation with linked-list

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.head == None

    def enQueue(self, data):
        newNode = Node(data)
        if self.tail == None:
            self.head = self.tail = newNode
            self.count += 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.count += 1

    def deQueue(self):
        if self.tail == None:
            print("Error: Queue is empty")
            return
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        self.count -= 1

    def peekFront(self):
        if self.head == None:
            return "No elements in the queue"
        return self.head.data

    def peekBack(self):
        if self.tail == None:
            return "No elements in the queue"
        return self.tail.data
    
    def __len__(self):
        return self.count