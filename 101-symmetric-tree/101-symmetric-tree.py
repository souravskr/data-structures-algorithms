# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # check if root is None then return True
        if root is None:
            return True
        
        # Else check if left subtree and right subtree are mirrored
        return isMirror(root.left, root.right)
    
def isMirror(tree1, tree2):
    # Check if both are None return True, else return False
    if not tree1 or not tree2:
        return tree1 == tree2

    # Return False if node values are not equal
    if tree1.val != tree2.val:
        return False

    return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)
    