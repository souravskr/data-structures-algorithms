class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        size = len(number)
        
        result = 0
        
        for i in range(size):
            
            if number[i] == digit:
                result = max(result, int(number[:i] + number[i+1:]))
        return str(result)