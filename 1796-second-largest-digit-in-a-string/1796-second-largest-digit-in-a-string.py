class Solution:
    def secondHighest(self, txt: str) -> int:
        number = list(set(s for s in txt if s.isdigit()))
        
        number.sort()
        
        size = len(number)
        
        if size <= 1:
            return -1
        return int (number[-2])