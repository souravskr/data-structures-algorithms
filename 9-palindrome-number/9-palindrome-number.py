class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        if x < 0: 
            return False
        
        reversed = 0
        while x:
            left = x % 10
            x = x // 10
            reversed = reversed * 10 + left
        if reversed == temp:
            return True
        return False
            
            