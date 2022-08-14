class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if strs:
            
            min_s = min(strs)
            max_s = max(strs)
            
            for i, c in enumerate(min_s):
                if c != max_s[i]:
                    return min_s[:i]
            return min_s
        return None