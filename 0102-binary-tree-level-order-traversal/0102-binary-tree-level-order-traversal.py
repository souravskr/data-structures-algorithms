# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            q_len = len(queue)
            level = []
            for i in range(q_len):
                cur = queue.popleft()
                if cur:
                    level.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
            
            if level:
                res.append(level)
        
        return res
                