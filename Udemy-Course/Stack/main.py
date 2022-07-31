class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
        print('--')

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.top
        if self.length == 1:
            self.top = None
        else:
            self.top = self.top.next
            temp.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        temp = self.top
        if temp:
            self.top = new_node
            self.top.next = temp
            self.length += 1
            return True
        return False


my_stack = Stack(4)
my_stack.prepend(5)
my_stack.prepend(3)
my_stack.prepend(9)
my_stack.print_stack()
my_stack.pop_first()
my_stack.pop_first()
my_stack.print_stack()
