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
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def lookup(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return temp
        return None

    # Iterative Solution
    def dfs_iterative(self):
        res = []
        if self.root is None:
            return res
        stack = [self.root]
        while stack:
            curr_node = stack.pop()
            res.append(curr_node.value)
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
        return res

    def dfs_recursive(self):
        res = []
        if self.root is None:
            return res

        def traverse(curr_node):
            res.append(curr_node.value)
            if curr_node.left:
                traverse(curr_node.left)
            if curr_node.right:
                traverse(curr_node.right)

        traverse(self.root)
        return res

    def bfs(self):
        res = []
        if self.root is None:
            return res
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            res.append(cur_node.value)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return res

    def contains(self, value):
        if self.root is None:
            return None
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return temp
        return False

    def bfs_lookup(self, value):
        if self.root is None:
            return None
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.value == value:
                return True
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return False

    def dfs_lookup(self, value):
        if self.root is None:
            return False

        def traverse(node, val):
            if val == node.value:
                return True
            if node.left:
                traverse(node.left, val)
            if node.right:
                traverse(node.right, val)

        return traverse(self.root.left, value) or traverse(self.root.right, value)

    def dfs_lookup_1(self, node, target):
        if node is None:
            return False
        if node.value == target:
            return True
        return self.dfs_lookup_1(node.left, target) or self.dfs_lookup_1(node.right, target)

    def bfs_treesum(self):
        res = 0
        if self.root is None:
            return res
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            res += cur_node.value
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return res

    def dfs_treesum(self, node):
        if node is None:
            return 0
        return node.value + self.dfs_treesum(node.left) + self.dfs_treesum(node.right)

    def dfs_min_value(self, node):
        if node is None:
            return math.inf
        left_min = self.dfs_min_value(node.left)
        right_min = self.dfs_min_value(node.right)
        return min(node.value, left_min, right_min)

    # def dfs_max_root_to_leaf_path(self, node):
    #     if node is None:
    #         return 0
    #     if self.dfs_max_root_to_leaf_path(node.left) > self.dfs_max_root_to_leaf_path(node.right):
    #         return node.value + self.dfs_max_root_to_leaf_path(node.left)
    #     else:
    #         return node.value + self.dfs_max_root_to_leaf_path(node.right)

    # Another Solution of above
    def dfs_max_root_to_leaf_path(self, root):
        if root is None:
            return -math.inf
        if root.left is None and root.right is None:
            return root.value
        max_value = max(self.dfs_max_root_to_leaf_path(root.left), self.dfs_max_root_to_leaf_path(root.right))
        return root.value + max_value

    def height(self, root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if left_height > right_height:
            h = 1 + left_height
        else:
            h = 1 + right_height
        return max(left_height, right_height) + 1



my_tree = BinarySearchTree()
my_tree.insert(5)
my_tree.insert(4)
my_tree.insert(3)
my_tree.insert(6)
my_tree.insert(7)
print(my_tree.lookup(7))
print(my_tree.dfs_iterative())
print(my_tree.bfs())
print(my_tree.contains(9))
print(my_tree.bfs_lookup(6))
print(my_tree.dfs_lookup(9))

print(my_tree.dfs_lookup_1(my_tree.root, 9))
print(my_tree.bfs_treesum())
print(my_tree.dfs_treesum(my_tree.root))

print(my_tree.dfs_min_value(my_tree.root))

print(my_tree.dfs_max_root_to_leaf_path(my_tree.root))

alvin_tree = BinarySearchTree()
alvin_tree.insert(5)
alvin_tree.insert(3)
alvin_tree.insert(1)
alvin_tree.insert(11)
alvin_tree.insert(10)
alvin_tree.insert(12)
alvin_tree.insert(9)
print(alvin_tree.height(alvin_tree.root))

print(alvin_tree.height(alvin_tree.root))