class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
class Tree:
    def __init__(self, value = None):
        if value is None:
            self.root = None
        else:
            root = Node(value)
            self.root = root

    def _in_order_print(node):
        if node.left != None:
            Tree._in_order_print(node.left)
        print(node.value)
        if node.right != None:
            Tree._in_order_print(node.right)
    
    def _pre_order_print(node):
        print(node.value)
        if node.left != None:
            Tree._pre_order_print(node.left)
        if node.right != None:
            Tree._pre_order_print(node.right)
    
    def _post_order_print(node):
        if node.left != None:
            Tree._post_order_print(node.left)
        if node.right != None:
            Tree._post_order_print(node.right)
        print(node.value)

    def in_order_print(self):
        if self.root is None:
            return "empty"
        Tree._in_order_print(self.root)
        
    def pre_order_print(self):
        if self.root is None:
            return "empty"
        Tree._pre_order_print(self.root)
    
    def post_order_print(self):
        if self.root is None:
            return "empty"
        Tree._post_order_print(self.root)
    
    
    def _search(value, node):
        if node is None:
            return False
        
        if node.value == value:
            return True
        
        if value < node.value:
            return Tree._search(value, node.left)
        
        return Tree._search(value, node.right)
    
    def search(self, value, node = None):
        if self.root is None:
            return False
        return Tree._search(value, self.root)
    
    def _insert(value, node):
        if value < node.value:
            if node.left is None:
                left_child = Node(value, node)
                node.left = left_child
                return
            return Tree._insert(value, node.left)
        if value > node.value:
            if node.right is None:
                right_child = Node(value, node)
                node.right = right_child
                return
            return Tree._insert(value, node.right)
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        return Tree._insert(value, self.root)
        
tree = Tree()
tree.insert(4)
tree.insert(8)
tree.insert(5)
tree.insert(4)
tree.insert(3)

tree.in_order_print()
print("+++++++++++++++++++++++++++")
tree.pre_order_print()
print("+++++++++++++++++++++++++++")
tree.post_order_print()
for i in range(10):
    print(i, tree.search(i))