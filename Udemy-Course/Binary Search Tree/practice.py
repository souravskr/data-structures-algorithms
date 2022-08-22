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

    def remove(self, value):
        # look up the node with a track of previous node
        # if the targeted node does not have right node, then
        # edge case: check if the previous node is None, which means we are removing the root node.
        # then simply left node of the root will be the new root.
        # else -->
        pass



my_tree = BinarySearchTree()
my_tree.insert(9)
my_tree.insert(4)
my_tree.insert(20)
my_tree.insert(1)
my_tree.insert(6)
my_tree.insert(15)
my_tree.insert(170)

print(my_tree.lookup(9).value)
