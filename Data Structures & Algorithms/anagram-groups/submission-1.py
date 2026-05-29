class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hash = {}

        for word in strs:
            int_sign = [0]*26
            for letter in word:
                int_sign[ord(letter)-ord("a")] += 1
            int_sign = tuple(int_sign)
            
            if int_sign not in my_hash:
                my_hash[int_sign] = [word]
            else:
                my_hash[int_sign].append(word)

        return list(my_hash.values())