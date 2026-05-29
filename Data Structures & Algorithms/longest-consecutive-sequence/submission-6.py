class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chain_beg = set()
        for num in nums:
            if num-1 not in nums:
                chain_beg.add(num)
        
        max_length = 0 
        for num in nums:
            length = 0
            if num in chain_beg:
                temp = num 
                while temp in nums:
                    temp += 1
                    length += 1
                max_length = max(max_length,length)
        return max_length 
