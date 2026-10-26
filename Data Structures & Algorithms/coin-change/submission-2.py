class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(a):
            if a == 0:
                return 0
            if a in memo:
                return memo[a]
            best = float("inf")
            for c in coins:
                if c <= a:
                    best = min(best, 1 + dfs(a - c))
            memo[a] = best
            return best

        res = dfs(amount)
        return res if res != float("inf") else -1
