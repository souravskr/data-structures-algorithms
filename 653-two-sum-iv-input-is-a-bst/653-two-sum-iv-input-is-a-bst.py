# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        result = []

        def traverse(curr_node):
            if curr_node.left:
                traverse(curr_node.left)
            result.append(curr_node.val)
            if curr_node.right:
                traverse(curr_node.right)

        traverse(root)
        
        left = 0
        right = len(result) - 1
        
        while left < right:
            cur_sum = result[left] + result[right]
            
            if target > cur_sum:
                left += 1
            elif target < cur_sum:
                right -= 1
            else:
                return True
        return False