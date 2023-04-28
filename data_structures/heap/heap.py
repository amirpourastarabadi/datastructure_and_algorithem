from abc import ABC, abstractmethod

class Heap(ABC):
    def __init__(self, values = []) -> None:
        self.root = None
        self.nodes = [None]
        self.size = 1
        
        for item in values:
            self.insert(item)
    
    @abstractmethod
    def insert(self, value):
        pass
    
    @abstractmethod
    def get_top(self):
        pass

    def get_size(self):
        return self.size - 1

    def __str__(self) -> str:
        result = ''
        for i in range(1, self.get_size()):
            result += str(self.nodes[i]) + ', '
        return result

    def find_parent(self, child_index):
        return child_index // 2
    
    def find_siblings(self, parent):
        s1 = 2 * parent if (2 * parent < len(self.nodes)) else None
        s2 = s1 + 1 if (2 * parent + 1 < len(self.nodes)) else None
        return s1, s2
    
class MaxHeap(Heap):

    def __init__(self, values=[]) -> None:
        super().__init__(values)
        
    def insert(self, value):
        self.nodes.append(value)
        value_index = self.size
        self.size += 1
        parent_index = self.find_parent(value_index) 
        while value_index > 1 and self.nodes[value_index] > self.nodes[parent_index]:
            self.nodes[value_index], self.nodes[parent_index] = self.nodes[parent_index], self.nodes[value_index]
            value_index = parent_index
            parent_index = self.find_parent(value_index)

    def get_top(self):
        if self.size <= 1:
            raise Exception("Heap Is Empty.")
        
        parent = 1
        
        self.nodes[parent], head = self.nodes[self.size - 1], self.nodes[parent]
        
        del self.nodes[self.size - 1]
        
        siblings = self.find_siblings(parent)
        while siblings[0] is not None:
            max_index = parent

            if self.nodes[parent] < self.nodes[siblings[0]]:
                max_index = siblings[0]

            if siblings[1] is not None and self.nodes[max_index] < self.nodes[siblings[1]]:
                max_index = siblings[1]
            
            if parent == max_index:
                break

            self.nodes[parent], self.nodes[max_index] = self.nodes[max_index], self.nodes[parent]
            parent = max_index
            siblings = self.find_siblings(parent)

        self.size -= 1
        return head 
    
class MinHeap(Heap):

    def __init__(self, values=[]) -> None:
        super().__init__(values)
        
    def insert(self, value):
        self.nodes.append(value)
        value_index = self.size
        self.size += 1
        parent_index = self.find_parent(value_index) 
        while value_index > 1 and self.nodes[value_index] < self.nodes[parent_index]:
            self.nodes[value_index], self.nodes[parent_index] = self.nodes[parent_index], self.nodes[value_index]
            value_index = parent_index
            parent_index = self.find_parent(value_index)

    def get_top(self):
        if self.size <= 1:
            raise Exception("Heap Is Empty.")
        
        parent = 1
        
        self.nodes[parent], head = self.nodes[self.size - 1], self.nodes[parent]
        
        del self.nodes[self.size - 1]
        
        siblings = self.find_siblings(parent)
        while siblings[0] is not None:
            top_index = parent

            if self.nodes[parent] > self.nodes[siblings[0]]:
                top_index = siblings[0]

            if siblings[1] is not None and self.nodes[top_index] > self.nodes[siblings[1]]:
                top_index = siblings[1]
            
            if parent == top_index:
                break

            self.nodes[parent], self.nodes[top_index] = self.nodes[top_index], self.nodes[parent]
            parent = top_index
            siblings = self.find_siblings(parent)

        self.size -= 1
        return head 
    


print("################# MAX HEAP #################")
max_heap = MaxHeap([10,20,3,5,15,5,1,4])
print(max_heap)
print("get items from top: ")
for _ in range(max_heap.get_size()):
    print(max_heap.get_top(), end= '->')


print("\n\n################# MIN HEAP #################")
min_heap = MinHeap([10,20,3,5,15,5,1,4])
print(min_heap)
print("get items from top: ")
for _ in range(min_heap.get_size()):
    print(min_heap.get_top(), end= '->')
