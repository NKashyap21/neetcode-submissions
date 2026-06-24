# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        self.res = [[root,1]]
        def dfs(node,level):
            if not node:
                return 
            if level > self.res[-1][1]:
                self.res.append([node,level])
            
            dfs(node.right,level+1)
            dfs(node.left,level+1)
        
        dfs(root,1)
        return [node.val for node,lev in self.res]

