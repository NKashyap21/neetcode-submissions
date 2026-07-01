class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(path,curr_sum,start):
            if curr_sum == target:
                res.append(path[:])
                return 
            
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if curr_sum + candidates[i] > target:
                    return 
                
                path.append(candidates[i])
                dfs(path,curr_sum+candidates[i],i+1)
                path.pop()
        dfs([],0,0)
        return res