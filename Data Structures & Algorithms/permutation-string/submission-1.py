class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        if m < n:
            return False
        
        count_s1 = [0]*26
        for letter in s1:
            count_s1[ord(letter)-ord("a")] += 1
        
        count_s2 = [0]*26
        for i in range(0,n):
            count_s2[ord(s2[i]) - ord("a")] += 1
        if count_s2 == count_s1:
            return True 
        l = 0
        for r in range(n,m):
            if r - l + 1 > n:
                count_s2[ord(s2[l])-ord("a")] -= 1
                l += 1
            count_s2[ord(s2[r]) - ord("a")] += 1
            if count_s1 == count_s2:
                return True 
        return False 
            
