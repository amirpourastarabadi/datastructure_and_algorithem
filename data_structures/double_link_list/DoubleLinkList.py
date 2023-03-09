class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def push(self, data):
        self.size += 1
        new_node = Node(data)
        if self.is_empty():
            new_node.next = self.tail
            new_node.prev = self.head
            self.tail.prev = new_node
            self.head.next = new_node
            return
        self.head.next.prev = new_node
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next = new_node
        return
    
    def pushBack(self, data):
        if self.is_empty():
            return self.push(data)
        
        self.size += 1
        new_node = Node(data)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
    
    def insertAt(self, data, index = 0):
        if index == 0:
            return self.push(data)
        if index == self.size:
            return self.pushBack(data)
        
        if index > self.size:
            raise Exception('Index Out Of Range.')
        
        self.size += 1
        new_node = Node(data)
        current = self.head.next
        for _ in range(index):
            current = current.next
        
        current.prev.next = new_node
        new_node.next = current
        new_node.prev = current.prev
        current.prev = new_node

    def pop(self):
        if self.size == 0:
            raise Exception('List Is Empty')
        self.size -= 1
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def remove(self, index):
        if index > self.size:
            raise Exception("Index Out Of Range")
        if index == self.size:
            return self.pop()
        
        self.size -= 1
        current = self.head
        for _ in range(index):
            current = current.next
        
        current.next.prev = current.prev
        current.prev.next = current.next

    def is_empty(self):
        return self.head.next is self.tail
    
    def __str__(self) -> str:
        if self.is_empty():
            return "empty"
        result = ''
        current = self.head.next

        while current is not self.tail:
            result += str(current.data) + ' '
            current = current.next
        
        return result



