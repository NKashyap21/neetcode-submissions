class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D = defaultdict(list)
        for u,v in prerequisites:
            D[u].append(v)
        
        history = set()
        seen = set()
        def dfs(node):
            if node not in seen:
                seen.add(node)
                history.add(node)
                for nei in D[node]:
                    if nei in history:
                        return False
                    if dfs(nei) == False:
                        return False
                history.remove(node)

        
        for n in range(numCourses):
            res = dfs(n)
            if res == False:
                return False
        return True 
            
