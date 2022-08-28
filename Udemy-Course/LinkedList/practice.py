class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list_iterative(self):
        temp = self.head
        while temp:
            print(f'{temp.value} -->')
            temp = temp.next

    def print_list_recursive(self, head):
        temp = head
        if temp is None:
            return None
        print(temp.value)
        temp = temp.next
        self.print_list_recursive(temp)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return True
        temp = self.head
        prev = temp
        while temp:
            prev = temp
            temp = temp.next
        prev.next = new_node
        return True

    def linked_list_to_array(self):
        result = []

        def traverse(head):
            if head is None:
                return []
            result.append(head.value)
            traverse(head.next)

        traverse(self.head)
        return result

    def sum_list(self):
        def traverse(head):
            if head is None:
                return 0
            return head.value + traverse(head.next)

        return traverse(self.head)

    def find_node(self, val):
        def traverse(head, val):
            if head is None:
                return False
            if head.value == val:
                return True
            res = traverse(head.next, val)
            return res

        if traverse(self.head, val):
            return True
        return False

    def get_node_value(self, index):
        temp = self.head
        prev = temp
        start = 0
        while start <= index:
            if temp is None:
                return None
            prev = temp
            temp = temp.next
            start += 1
        return prev.value

    def get_node_value_recursive(self, index):
        def traverse(head, index):
            if head is None:
                return None
            if index == 0:
                return head.value
            return traverse(head.next, index - 1)

        return traverse(self.head, index)

    def reverse_list_iterative(self):
        temp = self.head
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        t = before
        while t:
            print(t.value)
            t = t.next

    @staticmethod
    def merge_two_list(list1, list2):
        dummy = Node(0)
        current = dummy

        while list1 and list2:
            if list1.value < list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        while current:
            print(current.value)
            current = current.next

        return dummy.next

    @staticmethod
    def zip_lists(list1, list2):
        dummy = Node(0)
        current = dummy

        count = 0
        while list1 and list2:
            if count % 2 != 0:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
            count += 1

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        temp = dummy.next
        while temp:
            print(temp.value)
            temp = temp.next

        return dummy.next

    @staticmethod
    def alivin_zip(head1, head2):
        tail = head1
        current1 = head1.next
        current2 = head2
        count = 0

        while current1 and current2:
            if count % 2 == 0:
                tail.next = current2
                current2 = current2.next
            else:
                tail.next = current1
                current1 = current1.next

            tail = tail.next
            count += 1

        if current1:
            tail.next = current1
        if current2:
            tail.next = current2

        temp = head1
        while temp:
            print(temp.value)
            temp = temp.next

        return head1


my_list = LinkedList()
my_list.append(4)
my_list.append(5)
my_list.append(8)
my_list.append(10)
# print(my_list.print_list_recursive(my_list.head))
print(my_list.linked_list_to_array())
# print(my_list.sum_list())
# print(my_list.find_node(11))
# print(my_list.get_node_value(3))
# print(my_list.get_node_value_recursive(3))
# print("--")
# my_list.reverse_list_iterative()
# print(my_list.print_list_iterative())

my_list1 = LinkedList()
my_list1.append(2)
my_list1.append(3)
my_list1.append(6)
my_list1.append(7)
# print(my_list1.print_list_recursive(my_list1.head))
print(my_list1.linked_list_to_array())

print("--")
zip_head = LinkedList.zip_lists(my_list.head, my_list1.head)
# print(my_list1.print_list_recursive(zip_head))
print("--")
# alvin_head = LinkedList.alivin_zip(my_list.head, my_list1.head)


print("--")
# merged_head = LinkedList.merge_two_list(my_list.head, my_list1.head)
# print(my_list1.print_list_recursive(merged_head))

print("--")
print(my_list.head.next.next.value)
