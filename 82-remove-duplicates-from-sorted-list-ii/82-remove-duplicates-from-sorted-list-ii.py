# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        res_temp = []
        
        while temp:
            res_temp.append(temp.val)
            temp = temp.next
        
        count = Counter(res_temp)
        res_list = [k for k, v in count.items() if v == 1]
        
        dum = ListNode()
        cur = dum
        
        for i in res_list:
            cur.next = ListNode(i)
            cur = cur.next
        
        return dum.next
        