class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            t = i 
            count = 0
            while t:
                t = t & (t-1)
                count += 1
            res.append(count)
        return res