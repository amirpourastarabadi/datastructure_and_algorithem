class Heap:
    def __init__(self, values = []) -> None:
        self.root = None
        self.nodes = [None]
        self.size = 1
        
        for item in values:
            self.insert(item)
        
    def minify(self):
        pass

    def maxify():
        pass
    
    def insert(self, value):
        self.nodes.append(value)
        value_index = self.size
        self.size += 1
        parent_index = self.find_parent(value_index) 
        while value_index > 1 and self.nodes[value_index] > self.nodes[parent_index]:
            self.nodes[value_index], self.nodes[parent_index] = self.nodes[parent_index], self.nodes[value_index]
            value_index = parent_index
            parent_index = self.find_parent(value_index)
    
    def find_parent(self, child_index):
        return child_index // 2
    
    def __str__(self) -> str:
        result = ''
        for i in self.nodes:
            result += str(i) + ', '
        return result
    
    def get_max(self):
        return self.nodes[1]
    
    def get_max(self):
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
    
    def find_siblings(self, parent):
        s1 = 2 * parent if (2 * parent < len(self.nodes)) else None
        s2 = s1 + 1 if (2 * parent + 1 < len(self.nodes)) else None
        return s1, s2
     
h = Heap()
h.insert(10)
h.insert(20)
h.insert(15)
h.insert(5)
h.insert(1)
h.insert(4)
print(h)

for _ in range(6):
    print(h.get_max())
    print(h)

h2 = Heap([10,20,15,5,1,4])
print(h2)

# for _ in range(8):
#     print(h.get_max())
#     print(h)
