class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num,0)+1
        for num in my_dict:
            if my_dict[num] > 1:
                return True
        return False