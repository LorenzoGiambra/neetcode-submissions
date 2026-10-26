class Solution:
    #def rob(self, nums: List[int]) -> int:
    #    dp = [0] * (len(nums) + 2)
    #    for i in range(len(nums)):
    #        dp[i + 2] = max(dp[i + 1], dp[i] + nums[i])
    #    return dp[-1]

    def rob(self, nums: List[int]) -> int:
        memo = {}

        def f(i):
            if i < 0:
                return 0
            if i not in memo:
                memo[i] = max(f(i - 1), f(i - 2) + nums[i])
            return memo[i]

        return f(len(nums) - 1)
