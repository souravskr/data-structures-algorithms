# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = collections.defaultdict(list)
        
        def dfs(node, level):
            if node is None:
                return 
            res[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)
        return res.values()
        
        
        
#         res = []
#         queue = collections.deque()
#         queue.append(root)
        
#         while queue:
#             q_len = len(queue)
#             level = []
#             for i in range(q_len):
#                 cur = queue.popleft()
#                 if cur:
#                     level.append(cur.val)
#                     queue.append(cur.left)
#                     queue.append(cur.right)
            
#             if level:
#                 res.append(level)
        
#         return res
                