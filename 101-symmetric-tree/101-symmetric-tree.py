# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
        
    def isMirror(self,t1, t2):
        if not t1 or not t2:
            return t1 == t2
        
        if t1.val != t2.val:
            return False
        
        return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
        
        # queue = [root]
#         res = []
#         def traverse(cur):
#             if cur.left is not None:
#                 traverse(cur.left)
#             res.append(cur.val)
#             if cur.right is not None:
#                 traverse(cur.right)
#         traverse(root)
        
#         print(res)
        
#         size = len(res)
#         if size % 2 != 0:
#             mid = size // 2
#             right = size -1
#             for left in range(mid):
#                 if res[left] != res[right]:
#                     return False
#                 right -= 1
#             return True
#         else:
#             return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         while queue:
#             cur = queue.pop(0)
#             tree_arr.append(cur.val)
#             if cur.left is not None:
#                 queue.append(cur.left)
#             if cur.right is not None:
#                 queue.append(cur.right)
        
#         print(tree_arr)
#         res_dict = Counter(tree_arr[1:])
#         for k,v in res_dict.items():
#             if v != 2:
#                 return False
#         return True