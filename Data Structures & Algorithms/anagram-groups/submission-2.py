class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hash = {}

        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter)-ord("a")] += 1
            count = tuple(count)
            if count in my_hash:
                my_hash[count].append(word)
            else:
                my_hash[count] = [word]
        
        return list(my_hash.values())