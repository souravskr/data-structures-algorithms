class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(p):
            if len(p) ==1:
                return [p]    
            res=[]
            for j in range(0,len(p)):
                p[0],p[j]=p[j],p[0]
                res+=([[p[0]]+ x for x in dfs(p[1:])])
            return res
        return dfs(nums)