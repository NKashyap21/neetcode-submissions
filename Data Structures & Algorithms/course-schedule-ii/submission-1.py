class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        seen = set()
        done = set()
        D = defaultdict(list)
        for u,v in prerequisites:
            D[u].append(v)
        
        def dfs(node):
            if node in done:
                return True
            if node in seen:
                return False
            
            seen.add(node)
            for ne in D[node]:
                if not dfs(ne):
                    return False
            seen.remove(node)
            done.add(node)
            res.append(node)
            return True 

        for i in range(numCourses):
            x = dfs(i)
            if not x:
                return []
        return res 