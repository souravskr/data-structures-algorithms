class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_list(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
        print('---')

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.first
        self.first = temp.next
        temp.next = None
        self.length -= 1
        return temp


my_queue = Queue(2)
my_queue.push(3)
my_queue.push(4)
my_queue.print_list()
my_queue.pop()
my_queue.print_list()
