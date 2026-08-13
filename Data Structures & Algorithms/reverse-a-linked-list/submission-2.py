# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head 
        t = curr.next
        tmp = None 
        while t:
            curr.next = tmp 
            tmp = curr 
            curr = t 
            t = t.next 
        curr.next = tmp 
        return curr