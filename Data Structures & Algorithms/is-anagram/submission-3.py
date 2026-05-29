class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS,counterT={},{}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            counterS[s[i]] = counterS.get(s[i],0)+1
            counterT[t[i]] = counterT.get(t[i],0)+1
        
        if counterS==counterT:
            return True
        else:
            return False