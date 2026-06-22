# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count,max_count = 0 , 0
        def dfs(node,count):
            if not node:
                return
            nonlocal max_count 
            count +=1
            max_count = max(max_count,count)
            if node.left : dfs(node.left,count)
            if node.right : dfs(node.right,count)
        
        dfs(root,count)
        return max_count