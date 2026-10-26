class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def f(x):
            if x == n:
                return 1
            if x > n:
                return 0
            if x in memo:
                return memo[x]
            memo[x] = f(x+1) + f(x+2)
            return memo[x]
        return f(0)


        
                
        
