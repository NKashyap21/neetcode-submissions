class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D = defaultdict(list)
        for u,v in prerequisites:
            D[u].append(v)
        
        history = set()
        seen = set()
        def dfs(node):
            if node in seen:
                return False
            if D[node] == []:
                return True 
            seen.add(node)
            for nei in D[node]:
                if dfs(nei) == False:
                    return False
            seen.remove(node)
            D[node] = []
            return True 

        
        for n in range(numCourses):
            res = dfs(n)
            if res == False:
                return False
        return True 
            
