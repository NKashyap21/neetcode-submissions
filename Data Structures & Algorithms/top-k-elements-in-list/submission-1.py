class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hash = {}
        counter = [[] for _ in range(len(nums)+1)]
        result = []

        for num in nums:
            my_hash[num] = 1 + my_hash.get(num,0)
        
        for num,count in my_hash.items():
            counter[count].append(num)
        
        for i in range(len(counter)-1,0,-1):
            for n in counter[i]:
                result.append(n)
                if len(result) == k:
                    return result