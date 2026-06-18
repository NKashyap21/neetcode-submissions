class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow1,fast = 0,0
        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if slow1 == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow1 = nums[slow1]
            if slow2 == slow1:
                return slow1