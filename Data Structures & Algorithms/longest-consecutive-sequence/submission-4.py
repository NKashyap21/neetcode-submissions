class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        #[1,2,4,5,6,7] Ans=4 => [4,5,6,7]
        results = [] # [2,4] 
        length = 0
        
        for num in nums:
            temp = num
            while True:
                if temp in nums:
                    length+=1
                    temp+=1
                else:
                    results.append(length)
                    length = 0
                    break
        return max(results)
