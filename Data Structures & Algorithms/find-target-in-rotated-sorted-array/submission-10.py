class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        min_idx = l 

        if nums[min_idx] == target:
            return min_idx

        if nums[min_idx] < target <= nums[-1]:
            l,r = min_idx,len(nums)-1
        else:
            l,r = 0,min_idx-1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1

