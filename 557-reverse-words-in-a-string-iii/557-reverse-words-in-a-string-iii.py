class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join(str(item[::-1]) for item in s)  