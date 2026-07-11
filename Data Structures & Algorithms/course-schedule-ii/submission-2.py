class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen,cycle = set(),set()
        D = defaultdict(list)
        res = []

        for u,v in prerequisites:
            D[u].append(v)
        
        def dfs(node):
            if node in cycle:
                return False
            if node in seen:
                return True
            
            cycle.add(node)
            for ne in D[node]:
                if not dfs(ne):
                    return False
            
            cycle.remove(node)
            seen.add(node)
            res.append(node)
            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res 