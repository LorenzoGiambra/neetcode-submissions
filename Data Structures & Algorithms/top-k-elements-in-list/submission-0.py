from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        n = len(nums)
        buckets = [[] for i in range(n+1)]
        for num, fr in freq.items():
            buckets[fr].append(num)
        res = []
        for f in range(n, 0, -1):
            for num in buckets[f]:
                res.append(num)
            if len(res) == k:
                return res

            




