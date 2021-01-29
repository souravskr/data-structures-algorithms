from typing import List


class Stack:

    def __init__(self) -> None:
        self.a_list = list()

    def push(self, item):
        return self.a_list.append(item)

    def pop(self):
        if len(self.a_list) > 0:
            return self.a_list.pop()
        return None

    def __str__(self) -> str:
        return f"{self.a_list}"


mystack = Stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)
mystack.push(6)

print(mystack)
print(mystack.a_list)

mystack.pop()
mystack.pop()
mystack.pop()

print(mystack)
print(mystack.a_list)

mystack.pop()
mystack.pop()
mystack.pop()

print(mystack)
print(mystack.a_list)
