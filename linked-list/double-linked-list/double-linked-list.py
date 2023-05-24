class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def isEmpty(self):
        if self.head.next is None:
            return True
        return False
    
    def length(self):
        cur = self.head
        count = 0
        while cur.next != None:
            cur = cur.next
            count += 1
        return count
    
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def insert(self, data, index):
        if index > self.length() or index < 0:
            self.append(data)
        else:
            new_node = Node(data)
            cur = self.head
            count = 0
            while count != index:
                cur = cur.next
                count += 1
            new_node.next = cur.next
            new_node.prev = cur
            cur.next.prev = new_node
            cur.next = new_node


    def deleteFirst(self):
        cur = self.head
        if cur.next is None:
            print('No Element to Remove, List is Empty')
        elif cur.next.next is None:
            cur.next = None
        else:
            cur = cur.next
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

    
    def deleteAt(self, index):
        if self.isEmpty():
            print('No Element to Remove, List is Empty')
        elif index == 0:
            self.deleteFirst()
        else:
            cur = self.head
            count = 0
            while count != index:
                cur = cur.next
                count += 1
            cur = cur.next
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        
    
    def displayData(self):
        data = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            data.append(cur.data)
        return data

