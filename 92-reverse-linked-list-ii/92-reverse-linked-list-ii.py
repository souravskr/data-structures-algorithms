# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_prev = dum = ListNode(val=0, next=head)
        cur = head
        i = j = 0
        while i < left-1:
            left_prev = left_prev.next
            cur = cur.next
            i += 1
        
        prev = None
        
        while j < (right-left+1):
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
            j += 1
        
        left_prev.next.next = cur
        left_prev.next = prev
        
        return dum.next