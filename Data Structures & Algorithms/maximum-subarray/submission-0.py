class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum,sum_ = -float('inf'),0
        for i in range(len(nums)):
            sum_ += nums[i]
            maxSum = max(maxSum,sum_)
            if sum_ < 0:
                sum_ = 0
        return int(maxSum)