"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        org_copy = {None:None}
        curr = head
        while curr:
            new_node = Node(curr.val)
            org_copy[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            org_copy[curr].next = org_copy[curr.next]
            org_copy[curr].random = org_copy[curr.random]

            curr = curr.next
        return org_copy[head]