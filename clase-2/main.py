from Tree import Tree
from Node import Node 

tree = Tree()

tree.insert(['root',['A','B','C']])
tree.insert(['B',['D','E']])
tree.insert(['A',['F']])
tree.insert(['Z','M'])


print(f'El nodo es {tree.root.children[0].data}')

node_to_find = Node('A')

level = 0
print(f'El nivel es {tree.find_level_n_ary(tree.root, node_to_find, level)}')

tree.Level_Order_traversal()