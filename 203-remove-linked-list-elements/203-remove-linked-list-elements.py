# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        while val in arr:
            index = arr.index(val)
            arr.pop(index)
        
        dummy_node = ListNode()
        new_node = dummy_node
        for i in arr:
            new_node.next = ListNode(val=i)
            new_node = new_node.next
        
        return dummy_node.next