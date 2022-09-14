# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        if root is None:
            return False
        queue = collections.deque([root])
        cur_res = set()
        while queue:
            cur_node = queue.popleft()
            res_of_target = target - cur_node.val
            if res_of_target not in cur_res:
                cur_res.add(cur_node.val)
            else:
                return True
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return False
    
#         result = []

#         def traverse(curr_node):
#             if curr_node.left:
#                 traverse(curr_node.left)
#             result.append(curr_node.val)
#             if curr_node.right:
#                 traverse(curr_node.right)

#         traverse(root)
        
#         left = 0
#         right = len(result) - 1
        
#         while left < right:
#             cur_sum = result[left] + result[right]
            
#             if target > cur_sum:
#                 left += 1
#             elif target < cur_sum:
#                 right -= 1
#             else:
#                 return True
#         return False