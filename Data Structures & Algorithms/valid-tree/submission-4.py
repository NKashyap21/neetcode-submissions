class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        seen = set()
        q = deque()
        D = defaultdict(list)

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        seen.add(0)
        q.append(0)

        while q:
            node = q.popleft()
            for nei in D[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        
        return len(seen) == n
