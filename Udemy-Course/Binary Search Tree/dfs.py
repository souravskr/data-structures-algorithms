import math


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def dfs_pre_order(self):
        res = []

        def traverse(node):
            res.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return res

    def dfs_post_order(self):
        res = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            res.append(node.value)

        traverse(self.root)
        return res

    def dfs_in_order(self):
        res = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            res.append(node.value)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return res

    def tree_sum(self):
        def traversal(node):
            if node is None:
                return 0
            return node.value + traversal(node.left) + traversal(node.right)
        return traversal(self.root)

    def min_value(self):
        def traverse(node):
            if node is None:
                return math.inf
            return min(node.value, traverse(node.left), traverse(node.right))
        return traverse(self.root)

    def max_value(self):
        def traverse(node):
            if node is None:
                return -math.inf
            return max(node.value, traverse(node.left), traverse(node.right))
        return traverse(self.root)

    def lookup(self, val):
        def traverse(node, target):
            if node is None:
                return False
            if node.value == target:
                return True
            return traverse(node.left, target) or traverse(node.right, target)
        return traverse(self.root, val)


alvin_tree = BinarySearchTree()
alvin_tree.insert(47)
alvin_tree.insert(21)
alvin_tree.insert(76)
alvin_tree.insert(18)
alvin_tree.insert(27)
alvin_tree.insert(52)
alvin_tree.insert(82)

print('DFS-Pre-Order: ', alvin_tree.dfs_pre_order())
print('DFS-Post-Order: ', alvin_tree.dfs_post_order())
print('DFS-In-Order: ', alvin_tree.dfs_in_order())
print('Tree Sum: ', alvin_tree.tree_sum())
print('Min Value: ', alvin_tree.min_value())
print('Max Value: ', alvin_tree.max_value())
print('Search For the Value 4: ', alvin_tree.lookup(4))
