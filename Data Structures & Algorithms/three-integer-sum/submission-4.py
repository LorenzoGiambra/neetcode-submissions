class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        seen = set()
        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                target = -nums[i]
                if (nums[j] + nums[k]) == target:
                    triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                    if triplet not in seen:
                        seen.add(triplet)
                        result.append(list(triplet))
                if (nums[j] + nums[k]) < target:
                    j += 1
                else:
                    k -= 1
        return result                 
