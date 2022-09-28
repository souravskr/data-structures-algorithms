class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        size = len(word)
        end = size - 1
        num = ''
        for i in range(size):
            if word[i].isdigit():
                num += word[i]
                if i == end:
                    num += ' '
            else:
                num += ' '
        res_lst = collections.Counter([int(x) for x in num.split()])
        return len(res_lst)