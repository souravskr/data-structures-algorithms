class Solution:
    def canConstruct(self, str1: str, str2: str) -> bool:
        res = ''
        copy_str = list(str2)
        for c in str1:
            if c in copy_str:
                res += c
                index = copy_str.index(c)
                copy_str.pop(index)
        if res == str1:
            return True
        return False