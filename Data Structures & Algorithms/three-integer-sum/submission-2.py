class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue 
            target = -nums[i]
            start,end = i+1,len(nums)-1
            while start < end:
                sum_ = nums[start] + nums[end]
                if sum_ < target:
                    start += 1
                elif sum_ > target:
                    end -= 1
                else:
                    result.append([nums[i],nums[start],nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -=1

        return result