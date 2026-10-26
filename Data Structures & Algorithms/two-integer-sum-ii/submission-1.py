class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            if s < target:
                l += 1
                r += 1
            else:
                if l == 0 and r == len(numbers):
                    r -= 1
                else:
                    l -= 1
            
        return None
            



            
        