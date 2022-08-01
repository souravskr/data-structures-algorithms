class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def char_to_dict(input_string):
            my_dict = {}
            for i in input_string:
                if i in my_dict:
                    continue
                else:
                    my_dict[i] = input_string.count(i)
            return my_dict

        s_dict = char_to_dict(s)
        t_dict = char_to_dict(t)

        if s_dict == t_dict:
            return True
        else:
            return False
