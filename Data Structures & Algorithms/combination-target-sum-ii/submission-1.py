class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(sol,curr_sum,start):
            if curr_sum == target:
                res.append(sol[:])
                return 
            
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if curr_sum + candidates[i]  > target:
                    continue 
                
                sol.append(candidates[i])
                backtrack(sol,curr_sum+candidates[i],i+1)
                sol.pop()
        
        backtrack([],0,0)
        return res