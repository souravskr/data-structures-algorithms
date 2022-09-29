# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive
        def new_head(cur, prev=None):
            if cur is None:
                return prev
            after = cur.next
            cur.next = prev
            return new_head(after, cur)
        return new_head(head)
    
    # Iterative
        
#         temp = head
        
#         before = None
        
        
#         while temp:
#             after = temp.next
#             temp.next = before
#             before = temp
#             temp = after
        

        
#         return before
        