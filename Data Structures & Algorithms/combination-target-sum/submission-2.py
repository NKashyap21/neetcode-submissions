class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(path,curr_sum,start):
            if curr_sum == target:
                res.append(path[:])
                return 
            
            for i in range(start,len(nums)):
                if curr_sum + nums[i] > target:
                    continue
                
                path.append(nums[i])
                dfs(path,curr_sum+nums[i],i)
                path.pop()
        dfs([],0,0)
        return res