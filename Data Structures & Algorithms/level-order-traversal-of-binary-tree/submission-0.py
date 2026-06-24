# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            temp = []
            for i in range(len(q)):
                temp.append(q[i].val)
            res.append(temp)

            temp_q = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left: temp_q.append(node.left)
                if node.right: temp_q.append(node.right)
            
            for i in range(len(temp_q)):
                q.append(temp_q[i])
            

        return res