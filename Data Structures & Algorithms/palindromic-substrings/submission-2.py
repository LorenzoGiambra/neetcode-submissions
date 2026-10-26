class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 1
        tot_c = 0 

        def expand(l, r):
            c = 0
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                c += 1
            return c
        
        for i in range(n):
            codd = expand(i, i)
            ceven = expand(i, i+1)
            tot_c += (codd + ceven)
        
        return tot_c
