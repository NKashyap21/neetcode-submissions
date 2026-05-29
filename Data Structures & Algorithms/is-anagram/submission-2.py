class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS,counterT = {},{}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            counterS[s[i]] = 1+counterS.get(s[i],0)
            counterT[t[i]] = 1+counterT.get(t[i],0)
        
        if counterS == counterT:
            return True
        else:
            return False