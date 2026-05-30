class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            target = -nums[i]
            start,end = i+1,len(nums)-1
            while start < end:
                sum_ = nums[start] + nums[end]
                if sum_ < target:
                    start += 1
                elif sum_ > target:
                    end -= 1
                else:
                    if [nums[i],nums[start],nums[end]] not in result:
                        result.append([nums[i],nums[start],nums[end]])
                    start += 1
                    end -= 1
        
        return result 