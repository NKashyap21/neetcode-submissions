class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = set()
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                start.add(num)
        
        res = 0
        for num in start:
            length = 1
            while num + 1 in nums:
                length += 1
                num +=1 
            res = max(res,length)

        return res 