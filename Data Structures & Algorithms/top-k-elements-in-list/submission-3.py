class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hash = {}
        my_arr = [0]*(len(nums)+1)
        for num in nums:
            my_hash[num] = my_hash.get(num,0)+1
        
        for num,count in my_hash.items():
            if my_arr[count] == 0:
                my_arr[count] = [num]
            else:
                my_arr[count].append(num)
        
        result = []
        for i in range(len(my_arr)-1,-1,-1):
            if len(result) == k:
                break 
            if my_arr[i] != 0:
                for num in my_arr[i]:
                    if len(result) == k:
                        break
                    result.append(num)
        return result 