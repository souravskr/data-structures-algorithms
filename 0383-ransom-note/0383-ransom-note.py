class Solution:
    def canConstruct(self, str1: str, str2: str) -> bool:
        str1_dict = Counter(str1)
        str2_dict = Counter(str2)
        res = ''
        for c in str1:
            if str1_dict[c] <= str2_dict[c]:
                res += c
                str1_dict[c] -= 1
                str2_dict[c] -= 1
            else:
                return False
        if res == str1:
            return True
        return False
    
        # str1_dict = Counter(str1)
        # str2_dict = Counter(str2)
        # res = ''
        # for c in str1:
        #     if str1_dict[c] <= str2_dict[c]:
        #         res += c
        #         str1_dict[c] -= 1
        #         str2_dict[c] -= 1
        # if res == str1:
        #     return True
        # return False
    
    
    
        # res = ''
        # copy_str = list(str2)
        # for c in str1:
        #     if c in copy_str:
        #         res += c
        #         index = copy_str.index(c)
        #         copy_str.pop(index)
        # if res == str1:
        #     return True
        # return False