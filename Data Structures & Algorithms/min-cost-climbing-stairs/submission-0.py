class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dfs(x):
            if x == n:
                return 0
            if x == n-1:
                return cost[-1]
            if x in memo:
                return memo[x]
            memo[x] = cost[x] + min(dfs(x+1), dfs(x+2))
            return memo[x]
        return min(dfs(0), dfs(1))


        