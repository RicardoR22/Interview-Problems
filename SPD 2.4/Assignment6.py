"""
Given a binary search tree, reverse the order of its values by modifying the nodes’ links.
"""

from BinaryTree import BinarySearchTree

def reverse_tree(tree):
    reverse(tree.root)

    return tree


def reverse(root):
    if root:
        temp = root.left
        root.left = root.right
        root.right = temp
        reverse(root.left)
        reverse(root.right)



items = [4, 2, 6, 1, 3, 5, 7]
tree = BinarySearchTree()

for item in items:
    tree.insert(item)

print('items pre-order:   {}'.format(tree.items_pre_order()))
reverse_tree(tree)
print('items pre-order:   {}'.format(tree.items_pre_order()))


""""
Given a binary tree containing numbers, find the maximum sum path
(the path that has the largest sum of node values).
The path may start and end at any node in the tree.
"""

def max_sum_path(tree):
    curr_node = tree.root
    path = []

    while curr_node:
        path.append(curr_node)
        curr_node = curr_node.right

    return path


items = [4, 2, 6, 1, 3, 5, 7]
tree2 = BinarySearchTree()

for item in items:
    tree2.insert(item)

print(max_sum_path(tree2))
