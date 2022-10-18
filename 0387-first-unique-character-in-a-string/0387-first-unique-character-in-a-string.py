class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = Counter(s)
        for c in s:
            if s_dict[c] == 1:
                return  s.index(c)
        return -1
        # for c in s:
        #     if s.count(c) == 1:
        #         return s.index(c)
        # return -1