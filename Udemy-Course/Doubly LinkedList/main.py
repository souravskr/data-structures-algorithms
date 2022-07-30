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


my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.print_list()