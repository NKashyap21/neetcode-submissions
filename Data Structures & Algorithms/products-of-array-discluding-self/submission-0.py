class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i,j,product = 0,0,1
        result = []
        while i <= len(nums)-1:
            if j == len(nums)-1:
                if i!= j:
                    product *= nums[j]
                result.append(product)
                product=1
                j = 0
                i += 1
            if i == j:
                j += 1
                continue
            product *= nums[j]
            j += 1
        return result