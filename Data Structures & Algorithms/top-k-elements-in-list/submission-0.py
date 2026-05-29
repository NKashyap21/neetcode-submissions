class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hash = {}
        final_list = []
        temp = 0
        for num in nums:
            my_hash[num] = 1+my_hash.get(num,0)
        if len(my_hash) == 1:
            for x in my_hash:
                final_list.append(x)
                return final_list
        
        while len(final_list) <k:
            for x in my_hash:
                if my_hash[x] > temp:
                    temp = my_hash[x]
            key = [k for k,v in my_hash.items() if v==temp][0]
            print(key)
            final_list.append(key)
            my_hash.pop(key)
            temp = 0
        return final_list