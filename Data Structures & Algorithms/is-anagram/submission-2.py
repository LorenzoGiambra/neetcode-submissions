class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ls = {}
        lt = {}
        for ch in s:
            ls[ch] = ls.get(ch, 0) + 1
        for ch in t:
            lt[ch] = lt.get(ch, 0) + 1
        if ls == lt:
            return True
        return False

        