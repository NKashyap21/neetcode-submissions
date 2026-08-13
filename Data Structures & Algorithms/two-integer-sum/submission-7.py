class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        for i,num in enumerate(nums):
            if target-num in my_hash:
                if my_hash[target-num] == i:
                    continue
                return [my_hash[target-num],i]
            my_hash[num] = i 