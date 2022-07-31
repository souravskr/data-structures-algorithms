# Doubly LinkedList Can traverse both directions (Backward + Forward)
# Therefore, there will extra pointer for each node to point the previous node compared to singly LinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        mid = int(self.length / 2)
        if index < mid:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        left_node = self.get(index - 1)
        right_node = left_node.next

        new_node.prev = left_node
        new_node.next = right_node

        left_node.next = new_node
        right_node.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        left_node = temp.prev
        right_node = temp.next

        left_node.next = right_node
        right_node.prev = left_node

        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.pop()
my_doubly_linked_list.prepend(1)
# my_doubly_linked_list.pop_first()
# print(my_doubly_linked_list.get(2))

my_doubly_linked_list.print_list()
print('--')
my_doubly_linked_list.set_value(0, 5)
my_doubly_linked_list.print_list()
print('--')
my_doubly_linked_list.insert(1, 19)
my_doubly_linked_list.print_list()
print('--')
my_doubly_linked_list.remove(3)
my_doubly_linked_list.print_list()
