class Solution:
    def isValid(self, s:str) -> bool:
        closing_to_opening = {
        ')': '(',
        '}': '{',
        ']': '['
    }
        stack = []
        for c in s:
            if c in closing_to_opening:
                if stack and stack[-1] == closing_to_opening[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True