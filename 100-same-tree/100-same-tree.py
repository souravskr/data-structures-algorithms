# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            print(stack)
            c_p, c_q = stack.pop()
            if c_p and c_q and c_p.val == c_q.val:
                stack.append((c_p.right, c_q.right))
                stack.append((c_p.left, c_q.left))
            elif c_p != c_q:
                return False
            
        return True
            