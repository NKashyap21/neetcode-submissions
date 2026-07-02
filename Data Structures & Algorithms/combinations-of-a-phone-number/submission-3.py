class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numChar = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        res = []
        def dfs(i,currString):
            if len(currString) == len(digits):
                res.append(currString)
                return
            
            for c in numChar[int(digits[i])]:
                dfs(i+1,currString+c)
        
        if digits:
            dfs(0,"")
        return res