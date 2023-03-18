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
    
    def _findNode(node, value):
        if node is None:
            return None
        
        if node.value == value:
            return node
        
        if value < node.value:
            return Tree._findNode(node.left, value)
        
        return Tree._findNode( node.right, value)

    def remove(self, value):
        target_node = Tree._findNode(self.root, value)
        if target_node is None:
            return

        if target_node.right is not None:
            target_node.right.parent = target_node.parent
            if target_node.value > target_node.parent.value:
                target_node.parent.right = target_node.right
            else:
                target_node.parent.left = target_node.right
            return
        
        if target_node.left is not None:
            target_node.left.parent = target_node.parent
            if target_node.value > target_node.parent.value:
                target_node.parent.right = target_node.left
            else:
                target_node.parent.left = target_node.left
            return
        
        if target_node.value > target_node.parent.value:
            target_node.parent.right = None
            return
        
        target_node.parent.left = None
        
    
    
tree = Tree()
tree.insert(4)
tree.insert(8)
tree.insert(5)
tree.insert(4) # does not insert because of duplication
tree.insert(3)

# tree.in_order_print()
# print("+++++++++++++++++++++++++++")
# tree.pre_order_print()
# print("+++++++++++++++++++++++++++")
# tree.post_order_print()
# print("+++++++++++++++++++++++++++")
for i in range(10):
    print(i, tree.search(i))

tree.remove(8)

# print("+++++++++++++++++++++++++++")
# tree.post_order_print()
print("+++++++++++++++++++++++++++")
for i in range(10):
    print(i, tree.search(i))
