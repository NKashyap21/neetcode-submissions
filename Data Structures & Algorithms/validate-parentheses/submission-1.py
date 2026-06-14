class Solution:
    def isValid(self, s: str) -> bool:
        myHash = {"(":")","[":"]","{":"}"}
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            
            if s[i] == myHash.get(stack[-1],""):
                stack.pop()
            else:
                stack.append(s[i])
        
        return len(stack)==0