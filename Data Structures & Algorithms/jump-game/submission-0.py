class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def end(i):
            if i >= len(nums)-1:
                return True
            if nums[i] == 0:
                return False
            for j in range(nums[i],0,-1):
                if  end(i+j):
                    return True 
            return False 
        
        return end(0)