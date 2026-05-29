class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hash = {}
        result = []

        for string in strs:
            counter = [0]*26
            for letter in string:
                counter[ord(letter) -ord("a")] +=1
            counter = tuple(counter)

            if counter in my_hash:
                my_hash[counter].append(string)
            else:
                my_hash[counter] = [string]
        
        for x in my_hash:
            result.append(my_hash[x])
        return result