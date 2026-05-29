class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums = set(nums)
        results = []
        for num in nums:
            length = 0
            if num-1 not in nums:
                temp = num
                while True:
                    if temp in nums:
                        length+=1
                        temp += 1
                    else:
                        results.append(length)
                        break 
        return max(results)