class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end > 0 and s[end] == ' ':
            end -= 1
        beg = end
        while beg >= 0 and s[beg] != ' ':
            beg -= 1
        return end - beg
    
    
        # new_s = ' '.join(s.split())
        # s_list = [i for i in new_s.split()]
        # print(s_list)
        # return len(s_list[-1])