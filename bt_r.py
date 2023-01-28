class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def find_level_n_ary(root, node, level):
    if root is None:
        return 0
    if root.value == node.value:
        return level
    level += 1
    for child in root.children:
        level = find_level_n_ary(child, node, level)
        if level:
            return level
    return 0

# Creación del árbol
root = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)
child4 = Node(5)
child5 = Node(6)
child6 = Node(7)
child7 = Node(8)
root.children = [child1, child2, child3]
child1.children = [child4, child5]
child4.children = [child6, child7]

# Búsqueda del nivel del nodo con valor 6
node_to_find = Node(6)
level = find_level_n_ary(root, node_to_find, 0)
print("El nivel del nodo con valor", node_to_find.value, "es", level)