class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        reg = 0
        max_reg = 0
        while l < r:
            reg = (r - l) * min(heights[r], heights[l])
            if reg >= max_reg:
                max_reg = reg
            if heights[l] <= heights[r]:
                l += 1
                continue
            if heights[l] > heights[r]:
                r -= 1
                continue
        return max_reg


            

        