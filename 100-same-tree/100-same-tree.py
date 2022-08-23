# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p and q is None or q and p is None:
            return False
        elif p is None and q is None:
            return True
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # DFS - Iterative
#         stack = [(p, q)]
#         while stack:
#             print(stack)
#             c_p, c_q = stack.pop()
#             if c_p and c_q and c_p.val == c_q.val:
#                 stack.append((c_p.right, c_q.right))
#                 stack.append((c_p.left, c_q.left))
#             elif c_p != c_q:
#                 return False
            
#         return True
            