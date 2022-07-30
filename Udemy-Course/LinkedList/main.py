"""
Class LinkedList:
    def __init__(self, value):
        create new Node
    def append(self, value):
        create new Node
        add Node to the end
    def prepend(self, value):
        create new Node
        add Node at the beginning
    def insert(self, index, value):
        create new Node
        insert the Node at the index
"""

# LINKED LIST UNDER THE HOOD
'''
head: {
        'value': 4,
        'next': {
            'value': 5,
            'next': {
                'value': 6,
                'next': None
            }
        }
    }
'''


# EACH NODE CONSISTS OF A VALUE AND POINTER (NEXT).
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            pre = self.head
            self.head = new_node
            new_node.next = pre
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


my_linked_list = LinkedList(1)
my_linked_list.append(2)
# my_linked_list.append(6)
my_linked_list.print_list()
print('--')

my_linked_list.prepend(3)
my_linked_list.prepend(4)
my_linked_list.print_list()

print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
my_linked_list.print_list()
print('--')
my_linked_list.prepend(4)
my_linked_list.print_list()
