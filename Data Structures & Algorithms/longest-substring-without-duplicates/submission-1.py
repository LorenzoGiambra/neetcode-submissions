class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        longest = 0
        strings = set()
        for r in range(n):
            while s[r] in strings:
                strings.remove(s[l])
                l += 1
            strings.add(s[r])
            longest = max(longest, r-l+1)
        return longest