class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N+1)]

        def find(x):
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return par[x]
        
        def union(x1,x2):
            p1,p2 = find(x1),find(x2)
            if p1 == p2:
                return False
            par[p1] = p2
            return True 
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]