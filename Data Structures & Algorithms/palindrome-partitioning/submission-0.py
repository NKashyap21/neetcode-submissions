class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(path,i):
            if i == len(s):
                res.append(path[:])
                return 
            
            for j in range(i,len(s)):
                piece = s[i:j+1]
                if self.isPal(piece):
                    path.append(piece)
                    dfs(path,j+1)
                    path.pop()
            
        dfs([],0)
        return res
    
    def isPal(self,s):
        l,r = 0 ,len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l,r = l+1,r-1
        
        return True
