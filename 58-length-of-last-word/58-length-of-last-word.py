class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = ' '.join(s.split())
        s_list = [i for i in new_s.split()]
        print(s_list)
        return len(s_list[-1])