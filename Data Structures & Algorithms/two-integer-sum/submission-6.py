class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}

        for i,num in enumerate(nums):
            if num in my_hash:
                if nums[my_hash[num]] + num == target:
                    return [my_hash[num],i] 
            my_hash[num] = i
            left_over = target-num
            if left_over in my_hash and my_hash[left_over] != i:
                return [my_hash[left_over],my_hash[num]]