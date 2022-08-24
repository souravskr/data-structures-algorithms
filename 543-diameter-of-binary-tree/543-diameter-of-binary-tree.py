# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # O(n^2) Solution
        
        def height(node):
            if node is None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            return max(left_height, right_height) + 1
        
        if root is None: return 0
        
        left_height = height(root.left)
        right_height = height(root.right)
        
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        return max(left_height + right_height, max(left_diameter, right_diameter))
        
        
        
        
        