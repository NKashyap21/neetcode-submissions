import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')
        lo,hi = 1,max(piles)
        while lo <= hi:
            m = (lo+hi)//2
            numHours = 0
            for pile in piles:
                numHours += math.ceil(pile/m)
            if numHours  > h:
                lo = m+1
            elif numHours <= h:
                hi = m-1
                res = min(res,m)
        return res
