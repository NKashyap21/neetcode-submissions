class Solution:
    def climbStairs(self, n: int) -> int:
        #ways[n] = ways[n-1] + ways[n-2]
        if n == 1: return 1
        if n == 2: return 2
        prev,curr = 1,2
        for _ in range(2,n):
            prev,curr = curr,prev+curr

        return curr