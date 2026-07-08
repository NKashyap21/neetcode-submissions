from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D = defaultdict(list)
        for i in range(numCourses):
            D[i]
        
        for u,v in prerequisites:
            D[u].append(v)
        
        seen = set()
        history = set()

        

        def dfs(node,history):
            for nei_node in D[node]:
                if nei_node in history:
                    return False
                if nei_node not in seen:
                    seen.add(nei_node)
                    history.add(nei_node)
                    if dfs(nei_node,history) == False:
                        return False
                    history.remove(nei_node)

        for u in D:
            res = dfs(u,history)
            if res == False:
                return False
            
        return True 