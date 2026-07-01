class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s):
            if len(s) == 2*n and self.isValid(s):
                res.append(s)
                return 
            
            for char in ["(",")"]:
                if len(s) + 1 > 2*n:
                    return 
                temp = s
                s += char
                dfs(s)
                s = temp

        dfs('')
        return res        


    def isValid(self,s):
        myStack = []
        myHash = {"(":")"}
        for char in s:
            if not myStack:
                myStack.append(char)
            elif myHash.get(myStack[-1],"") == char:
                myStack.pop()
            else:
                myStack.append(char)
        return len(myStack) == 0