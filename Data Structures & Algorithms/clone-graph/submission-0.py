"""
import copy
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        D = defaultdict(Node)
        seen = set()

        def dfs(node):
            if not node:
                return 
            if node not in seen:
                seen.add(node)
                temp = Node(val = node.val)
                D[node] = temp
                for nei in node.neighbors:
                    dfs(nei)
        
        dfs(node)

        i = 0
        copyNode = Node()
        for old,new in D.items():
            if i == 0:
                copyNode = new
                i += 1
            for neighbors in old.neighbors:
                new.neighbors.append(D[neighbors])
        return copyNode


