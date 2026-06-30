class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #Base condition : if len(sol) == len(nums)
        #Choices : the num in nums
        #Constraint : num shouldn't be sol twice
        #BackProp step

        res = []
        def backtrack(sol):
            if len(sol) == len(nums):
                res.append(sol[:])
                return 
            
            for num in nums:
                if num in sol:
                    continue
                
                sol.append(num)
                backtrack(sol)
                sol.pop()
        
        backtrack([])
        return res 