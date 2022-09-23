class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return True

        temp = self.head
        pre = temp
        while temp:
            pre = temp
            temp = temp.next
        pre.next = new_node
        return True

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

    def middle_node(self):
        size = 0
        temp = self.head
        while temp:
            size += 1
            temp = temp.next
        if size % 2 != 0:
            mid = size // 2
            i = 1
            temp1 = self.head
            while i <= mid:
                temp1 = temp1.next
                i += 1
            return temp1.val
        else:
            mid = (size // 2)
            j = 1
            temp2 = self.head
            while j <= mid:
                temp2 = temp2.next
                j += 1
            return temp2.next.val







my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.print_list()
