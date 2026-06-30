class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]

        def backtrack(sol,curr_sum,start):
            if curr_sum == target:
                res.append(sol[:])
                return 
            
            for i in range(start,len(nums)):
                if curr_sum + nums[i] > target:
                    continue
                
                sol.append(nums[i])
                backtrack(sol,curr_sum + nums[i],i)
                sol.pop()
        backtrack(sol,0,0)
        return res