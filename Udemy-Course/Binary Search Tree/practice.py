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


my_tree = BinarySearchTree()
my_tree.insert(5)
my_tree.insert(4)
my_tree.insert(3)
my_tree.insert(6)
my_tree.insert(7)
print(my_tree.lookup(7))
print(my_tree.dfs_iterative())
