class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        for index,num in enumerate(nums):
            if num in my_hash and 2*num == target:
                x = my_hash[num]
                my_hash[num] = index
                return [x,index]
            my_hash[num] = index
            if target-num in my_hash and my_hash[num] != my_hash[target-num]:
                return [my_hash[target-num],my_hash[num]]