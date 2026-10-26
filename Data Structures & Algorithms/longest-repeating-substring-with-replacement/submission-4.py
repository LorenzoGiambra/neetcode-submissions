class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0 
        best = 0
        for r, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            maxf = max(maxf, count[ch])
            while (r - l + 1) - maxf > k:
                left_ch = s[l]
                count[left_ch] -= 1
                l += 1
            best = max(best, r-l+1)
        return best
            
            
        


        