class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def cS(n):
            if n in memo:
                return memo[n]
            if n == 1: return 1 
            if n == 2: return 2 

            res =  cS(n-1) + cS(n-2)
            memo[n] = res
            return res 
        return cS(n)
