class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictio = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in dictio:
                return [dictio[diff], i]
            dictio[x] = i
            
        