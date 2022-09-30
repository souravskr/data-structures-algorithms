# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Find Middle of the List
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse the second half of the list
        prev, cur = None, slow.next
        while cur:
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        slow.next = None
 
        # Merge first and second half of the list
        head1, head2 = head, prev
        while head2:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp
    
        # Solution: 1
#         s = head
#         f = head.next
        
#         while f and f.next:
#             s = s.next
#             f = f.next.next
        
#         temp = s.next
#         s.next = None
#         before = None
        
#         while temp:
#             after = temp.next
#             temp.next = before
#             before = temp
#             temp = after
        
#         first = head
#         second = before
        
#         while second:
#             temp_1 = first.next
#             temp_2 = second.next
#             first.next = second
#             second.next = temp_1
#             first = temp_1 
#             second = temp_2
        