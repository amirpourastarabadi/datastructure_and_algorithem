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
        
        # if target_node has no children
        if target_node.left is None and target_node.right is None:
            if target_node.value > target_node.parent.value:
                target_node.parent.right = None
            else:
                target_node.parent.left = None
            return

        # if target_node has only one child
        if (target_node.left is None and target_node.right is not None) or (target_node.left is not None and target_node.right is None):
            if target_node.right is not None:
                if target_node.value > target_node.parent.value:
                    target_node.parent.right = target_node.right
                else:
                    target_node.parent.left = target_node.right
            else:
                if target_node.value > target_node.parent.value:
                    target_node.parent.right = target_node.left
                else:
                    target_node.parent.left = target_node.left
            return
        
        # if target_node has two children
        most_right_of_left_child = Tree._findMostRight(target_node.left)
        if most_right_of_left_child.left is None:
            target_node.value = most_right_of_left_child.value
            most_right_of_left_child.parent.right = None
            return
        else:
            target_node.value = most_right_of_left_child.value
            most_right_of_left_child.parent.right = most_right_of_left_child.left
            return
    
    def _findMostRight(node):
        if node.right is None:
            return node
        return Tree._findMostRight(node.right)
    
    def _findMostLeft(node):
        if node.left is None:
            return node
        return Tree._findMostLeft(node.left)
    
    def max(self):
        return Tree._findMostRight(self.root)
    
    def min(self):
        return Tree._findMostLeft(self.root)

    def nearestAncestor(self, node1, node2):
        if node1 is None or node2 is None:
            raise Exception('node1 and node2 are not in the same tree.')
        if Tree._search(node2.value, node1.parent):
            return node1.parent
        return self.nearestAncestor(node1.parent, node2)
        
    
    
tree = Tree()
tree.insert(4)
tree.insert(8)
tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(3.5)
tree.insert(9)
tree.insert(10)
tree.insert(9.5)
tree.insert(8.8)
tree.insert(8.5)
tree.insert(6)
tree.insert(4.9)

l = list(range(11))
l.extend([3.5, 9.5, 4.9, 8.5])

for i in l:
    print(i, tree.search(i))


print("+++++++++++++++++++++++++++")
for i in l:
    print(i, tree.search(i))
print("+++++++++++++++++++++++++++")
print('max = ', tree.max().value)
print('min = ', tree.min().value)
print("+++++++++++++++++++++++++++")
n1 = Tree._findNode(tree.root, 4)
n2 = Tree._findNode(tree.root, 4)
print('nearest ancestor = ', tree.nearestAncestor(n1, n2).value)