import collections


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryLinedList:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if value == temp.value:
                return False

            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def find_target(self, target):
        if self.root is None:
            return False
        queue = collections.deque([self.root])
        cur_res = set()
        while queue:
            cur_node = queue.popleft()
            res_of_target = target - cur_node.value
            if res_of_target not in cur_res:
                cur_res.add(cur_node.value)
            else:
                return True
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return False


my_tree = BinaryLinedList()
my_tree.insert(0)
my_tree.insert(-1)
my_tree.insert(2)
my_tree.insert(-3)
my_tree.insert(4)


print(my_tree.find_target(-4))
