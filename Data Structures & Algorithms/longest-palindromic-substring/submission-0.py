class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        bestL, bestR = 0,1

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r    #s[l+1:r]     

        for i in range(n):
            l1, r1 = expand(i, i)
            if r1-l1 > bestR-bestL:
                bestL, bestR = l1, r1
                
            l2, r2 = expand(i, i+1)
            if r2-l2 > bestR-bestL:
                bestL, bestR = l2, r2
        
        return s[bestL:bestR]