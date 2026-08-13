import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')
        
        l,r = 1,max(piles)
        while l <= r:
            k = (l+r) // 2
            eating_time = 0
            for pile in piles:
                eating_time += math.ceil(pile / k)
            if eating_time > h:
                l = k+1
            elif eating_time <= h:
                res = min(res,k)
                r = k - 1
        return res 
        