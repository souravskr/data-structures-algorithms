class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_size = len(s1)
        s2_size = len(s2)
        if s1_size > s2_size:
            return False
        s1 = ''.join(sorted(s1))

        for i in range(s2_size - s1_size + 1):
            new_str = ''.join(sorted(s2[i:i+s1_size]))
            if s1 == new_str:
                return True
        return False
        
#         def char_to_dict(s):
#             res = {}
#             for i in range(len(s)):
#                 res[s[i]] = ord('a') - ord(s[i])
#             return res
        
#         s1_size = len(s1)
#         s2_size = len(s2)
#         if s1_size > s2_size:
#             return False
#         s1_dict = char_to_dict(s1)
#         for i in range(s2_size - s1_size + 1):
#             temp_dict = char_to_dict(s2[i:i+s1_size])
#             if s1_dict == temp_dict:
#                 return True
#         return False
        
        
        
        
        
#         def string_to_dict(s):
#             s_dict = {}
#             i = 1
#             for c in s:
#                 if c in s_dict:
#                     s_dict[c] += 1
#                 else:
#                     s_dict[c] = i
#             return s_dict

#         if len(s1) > len(s2):
#             return False
#         s_dict = string_to_dict(s1)
#         s1_size = len(s1)
#         size = len(s2) - s1_size
#         matched = False

#         for i in range(size+1):
#             if s_dict == string_to_dict(s2[i:s1_size + i]):
#                 matched = True
#         return matched
    