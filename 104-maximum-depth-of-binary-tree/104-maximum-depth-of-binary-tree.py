# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
        
#         curr_node = root
#         stack = [[root, 1]]
#         result = 1
        
#         while stack:
#             node, level = stack.pop()
#             if node:
#                 result = max(result, level)
#                 stack.append([node.left, level + 1])
#                 stack.append([node.right, level + 1])
#         return result
        