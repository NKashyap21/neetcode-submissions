import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo,hi = 1,max(piles)
        res = float('inf')
        while lo <= hi:
            m = (lo+hi)//2
            numHours = 0
            for pile in piles:
                numHours += math.ceil(pile/m)
            if numHours > h:
                lo = m+1
            elif numHours <= h:
                res = min(res,m)
                hi = m-1
        return res 