class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
class Tree:
    def in_order_print(node):
        if node.left != None:
            Tree.in_order_print(node.left)
        print(node.value)
        if node.right != None:
            Tree.in_order_print(node.right)
    
    def pre_order_print(node):
        print(node.value)
        if node.left != None:
            Tree.pre_order_print(node.left)
        if node.right != None:
            Tree.pre_order_print(node.right)
    
    def post_order_print(node):
        if node.left != None:
            Tree.post_order_print(node.left)
        if node.right != None:
            Tree.post_order_print(node.right)
        print(node.value)

    def search(node, value):
        if node == None:
            return False
        
        if node.value == value:
            return True
        
        if value < node.value:
            return Tree.search(node.left, value)
        
        return Tree.search(node.right, value)
    
    def insert(node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            if node.left is None:
                left_child = Node(value, node)
                node.left = left_child
                return
            return Tree.insert(node.left, value)
        if value > node.value:
            if node.right is None:
                right_child = Node(value, node)
                node.right = right_child
                return
            return Tree.insert(node.right, value)
        
root = Tree.insert(None, 4)

Tree.insert(root, 8)
Tree.insert(root, 5)
Tree.insert(root, 4)
Tree.insert(root, 3)

Tree.in_order_print(root)
print("+++++++++++++++++++++++++++")
Tree.pre_order_print(root)
print("+++++++++++++++++++++++++++")
Tree.post_order_print(root)
for i in range(10):
    print(i, Tree.search(root, i))