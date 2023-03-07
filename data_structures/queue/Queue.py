

class Queue:

    def __init__(self, size):
        self.queue = [None] * size
        self.head  = 0
        self.tail  = 0
        self.num   = 0
        
    def dequeue(self):
        if self.num <= 0:
            raise Exception('Queue is empty')
        el = self.queue[self.head]
        self.head = (self.head + 1) % len(self.queue)   
        self.num -= 1
        return el

    def enqueue(self, el):
        if self.num >= len(self.queue):
            raise OverflowError('Queue is full')
        
        self.queue[self.tail] = el
        self.tail = (self.tail + 1) % len(self.queue)
        self.num += 1

    def front(self):
        if self.num == 0:
            return None
        return self.queue[self.head]
    
    def size(self):
        return self.num

    def is_empty(self):
        return self.size() == 0
    
    def is_full(self):
        return self.size() == len(self.queue)


queue = Queue(3);
queue.enqueue('amir')
print ('front of queue is', queue.front())
queue.enqueue('ali')
print ('front of queue is', queue.front())
queue.dequeue()
print ('front of queue is', queue.front())
queue.enqueue('feri')
queue.enqueue('kaveh')
print('queue is full?', queue.is_full())
queue.dequeue()
print('queue is full?', queue.is_full())
