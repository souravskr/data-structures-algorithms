class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)
        if s_dict == t_dict:
            return True
        return False
        # def string_to_dict(input_string):
        #     my_string = {}
        #     for c in input_string:
        #         if c in my_string:
        #             my_string[c] = input_string.count(c)
        #         else:
        #             my_string[c] = 0
        #     return my_string
        # s_dict = string_to_dict(s)
        # t_dict = string_to_dict(t)
        # if s_dict == t_dict:
        #     return True
        # return False
        