class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = float('inf')
        while l <= r:
            m = (l+r)//2
            numHours = 0
            for pile in piles:
                numHours += math.ceil(pile/m)
            
            if numHours > h:
                l = m+1
            else:
                r = m-1
                res = min(res,m)

        return res