class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # res_dict = defaultdict(list)
        # for c in s:
        #     if c in res_dict:
        #         res_dict[c].append(1)
        #         if len(res_dict[c]) == 2:
        #             return c
        #     else:
        #         res_dict[c].append(1)
        
        res = set()
        for c in s:
            if c in res:
                return c
            res.add(c)