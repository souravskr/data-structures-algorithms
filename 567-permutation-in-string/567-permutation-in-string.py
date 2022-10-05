class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_size = len(s1)
        s2_size = len(s2)
        if s1_size > s2_size:
            return False
        s1_dict = collections.Counter(s1)
        for i in range(s2_size - s1_size + 1):
            temp_dict = collections.Counter(s2[i:i+s1_size])
            if s1_dict == temp_dict:
                return True
        return False