class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        D = defaultdict(list)
        self.count = 0
        for u,v in edges:
            D[u].append(v)
            D[v].append(u)

        def dfs(node):
            if node in seen:
                return 
            seen.add(node)
            for ne in D[node]:
                dfs(ne)
        
        count=0
        for i in range(n):
            if i not in seen:
                dfs(i)
                count +=1
        return count
            

