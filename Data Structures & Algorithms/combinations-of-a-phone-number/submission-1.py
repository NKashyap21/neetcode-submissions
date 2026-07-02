class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numChar = {2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        res = []
        if not digits:
            return []
        def dfs(path,i):
            x = "".join(path)
            if len(x) == len(digits) and i == len(digits):
                res.append(x)
                return
            
            
            for char in numChar[int(digits[i])]:
                path.append(char)
                dfs(path,i+1)
                path.pop()
            
        
        dfs([],0)
        return res