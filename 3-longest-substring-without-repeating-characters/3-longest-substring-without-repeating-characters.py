class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = max_str = 0
        char_set = set()
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[j])
                j += 1
            char_set.add(s[i])
            max_str = max(max_str, i - j + 1)
        return max_str