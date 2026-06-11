class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        pivot = l 
        if target == nums[pivot]:
            return pivot
        
        if target >= nums[0]:
            l,r = 0,pivot-1
            if pivot-1 <0:
                r = len(nums)-1
        elif target <= nums[-1]:
            l,r=pivot+1,len(nums)-1
            if pivot+1 > len(nums):
                l = (pivot+1)%len(nums)
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m 
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        return -1 