"""
binary_tree = {
        'value': 4,
        'left': None,
        'right': None
    }
"""
"""
    binary_tree = {
        'value': 4,
        'left': {
            'value': 3,
            'left': None,
            'right': None
        },
        'right': {
            'value': 23,
            'left': None,
            'right': None
        }
    }
"""


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

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    @staticmethod
    def min_value_node(current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def minimum(self):
        temp = self.root
        value = temp.value
        while temp:
            value = temp.value
            temp = temp.left

        return value


my_binary_tree = BinarySearchTree()
my_binary_tree.insert(4)
my_binary_tree.insert(5)
my_binary_tree.insert(3)
my_binary_tree.insert(1)
print(my_binary_tree.root.value)
print(my_binary_tree.root.left.value)
print(my_binary_tree.root.left.left.value)
print(my_binary_tree.root.right.value)
print(f'Minimum: {my_binary_tree.min_value_node(my_binary_tree.root.left)}')
print(my_binary_tree.contains(0))
