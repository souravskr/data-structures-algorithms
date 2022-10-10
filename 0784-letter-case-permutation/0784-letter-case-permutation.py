class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        def helper(s, val):
            if not s:
                results.append(val)
                return
            if s[0] not in [str(i) for i in range(0,10)]:
                helper(s[1:], val + s[0].lower() )
                helper(s[1:], val + s[0].upper())
            else:
                helper(s[1:], val + s[0])        
        
        helper(s, "")
        return(results)