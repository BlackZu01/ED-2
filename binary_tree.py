class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self.print_tree(node.right, level + 1)

tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.print_tree(tree.root)