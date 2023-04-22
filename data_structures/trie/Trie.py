
class Node:
    def __init__(self, endOfString = False) -> None:
        self.branches = [None for _ in range(26)]
        self.endOfString = endOfString

class Branch:
    def __init__(self, value, start = None, end = None) -> None:
        self.value = value
        self.start = start
        self.end = end

class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, value):
        Trie._insert(value, self.root)

    def _insert(value, node, index = 0):
        if index == len(value):
            return
        
        asci = ord(value[index]) - ord('a')
        if node.branches[asci] == None:
            new_node = Node(endOfString= (index == len(value) - 1))
            node.branches[asci] = Branch(value[index], node, new_node)
            index += 1  
            return Trie._insert(value, new_node, index)
        
        index += 1  
        return Trie._insert(value, node.branches[asci].end, index)

    def search(self, value):
        return Trie._search(value, self.root)

    def _search(value, node, index = 0):
        if index == len(value):
            return node.endOfString
        
        asci = ord(value[index]) - ord('a')
        if node.branches[asci] == None:
            return False
        
        index += 1  
        return Trie._search(value, node.branches[asci].end, index)

    def remove(self, value):
        Trie._remove(value, self.root)

    def _remove(value, node, index = 0):
        if index == len(value):
            node.endOfString = False
            return None
        
        asci = ord(value[index]) - ord('a')
        if node.branches[asci] == None:
            return None
        
        index += 1  
        return Trie._remove(value, node.branches[asci].end, index)


    

tri = Trie()
tri.insert('a')
tri.insert('ab')
tri.insert('abc')
tri.insert('abd')
print('a = ', tri.search('a'))
print('ab = ', tri.search('ab'))
print('abc = ', tri.search('abc'))
print('abd = ', tri.search('abd'))
tri.remove('ab')
print('remove ab')
print('a = ', tri.search('a'))
print('ab = ', tri.search('ab'))
print('abc = ', tri.search('abc'))
print('abd = ', tri.search('abd'))
