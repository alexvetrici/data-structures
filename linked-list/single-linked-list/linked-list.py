class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def insert(self, index, data):
        if index < 0 or index > self.length():
            return self.append(data)
        new_node = Node(data)
        cur1 = self.head
        cur2 = cur1.next
        count = 0
        while count != index:
            cur1 = cur2
            cur2 = cur1.next
            count += 1
        cur1.next = new_node
        new_node.next = cur2

    def delete(self, index):
        if index > self.length():
            print('ERROR: Index out of range')
            return
        cur1 = self.head
        cur2 = cur1.next
        count = 0 
        while count != index:
            cur1 = cur2
            cur2 = cur1.next
            count += 1
        cur1.next = cur2.next

    def get(self, index):
        if index > self.length():
            print('ERROR: Index out of range')
            return
        data = self.displayData()
        return data[index]

    def length(self):
        length = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            length += 1
        return length

    def displayData(self):
        data = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            data.append(cur.data)
        return data