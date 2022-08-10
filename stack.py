from typing import List


class Stack:

    def __init__(self) -> None:
        self.a_list = []

    def push(self, item):
        return self.a_list.append(item)

    def pop(self):
        if len(self.a_list) > 0:
            return self.a_list.pop()
        return None

    def peek(self):
        if len(self.a_list) > 0:
            return self.a_list[-1]
        return None

    def __str__(self) -> str:
        return f"{self.a_list}"


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)

print(my_stack)
print(my_stack.a_list)

my_stack.pop()
my_stack.pop()
my_stack.pop()

print(my_stack)
print(my_stack.a_list)
print(my_stack.peek())

my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()

print(my_stack)
print(my_stack.a_list)
print(my_stack.peek())
