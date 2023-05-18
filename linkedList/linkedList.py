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

    def displayData(self):
        data = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            data.append(cur.data)
        return data





x = LinkedList()
x.append(3)
x.append(5)
print(x.displayData())