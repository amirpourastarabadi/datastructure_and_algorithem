class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.head = 0
    
    def push(self, el):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.stack[self.head] = el
        self.head += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self.head -= 1
        return self.stack[self.head]
    
    def is_full(self):
        return self.head == len(self.stack)
    
    def is_empty(self):
        return self.head == 0
    
    def top(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self.head
    
    def size(self):
        return self.head




stack = Stack(3)
stack.push('amir')
stack.push('ali')
print('stack size =', stack.size())
print("pop => ", stack.pop())
print('stack size =', stack.size())
stack.push('kaveh')
stack.push('feri')
try:
    stack.push('feri')
except OverflowError as e:
    print(e)
print("pop => ", stack.pop())
print("pop => ", stack.pop())
print("pop => ", stack.pop())
try:
    print("pop => ", stack.pop())
except Exception as e:
    print(e)

try:
    stack.push('kaveh1')
    print('push kaveh1')
    stack.push('kaveh2')
    print('push kaveh2')
    stack.push('kaveh3')
    print('push kaveh3')
    print('stack is full?', stack.is_full())
    print('try push kaveh4')
    stack.push('kaveh4')
    print('push kaveh4')
except OverflowError as e:
    print(e)