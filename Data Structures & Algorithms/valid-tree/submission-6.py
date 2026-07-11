class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cycle = set()
        D = defaultdict(list)
        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        def dfs(node,prev):
            if node in cycle:
                return False
            cycle.add(node)
            for ne in D[node]:
                if ne == prev:
                    continue
                if not dfs(ne,node):
                    return False
            return True 
        
        return dfs(0,-1) and len(cycle) == n