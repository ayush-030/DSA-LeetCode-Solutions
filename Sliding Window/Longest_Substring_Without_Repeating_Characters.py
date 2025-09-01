# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Pattern: Sliding Window Pattern (Two Pointers + Hashing)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        # Initializing First pointer
        l = 0
        result = 0
        # Initializing Second pointer in a loop
        for r in range (len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        return result