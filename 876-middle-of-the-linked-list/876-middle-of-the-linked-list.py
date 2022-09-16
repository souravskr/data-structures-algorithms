# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        # size = 0
        # temp = head
        # while temp:
        #     size += 1
        #     temp = temp.next
        # if size % 2 != 0:
        #     mid = size // 2
        #     i = 1
        #     temp1 = head
        #     while i <= mid:
        #         temp1 = temp1.next
        #         i += 1
        #     return temp1
        # else:
        #     mid = (size // 2)
        #     j = 1
        #     temp2 = head
        #     while j <= mid:
        #         temp2 = temp2.next
        #         j += 1
        #     return temp2