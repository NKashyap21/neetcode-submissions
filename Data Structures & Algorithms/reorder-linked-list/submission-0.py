# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head):
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head 
        head.next = None
        return new_head

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = slow.next
        slow.next = None 

        reversed_list = self.reverseList(head1)
        l1,l2 = head,reversed_list
        dummy = ListNode()
        curr = dummy 
        while l1 and l2:
            curr.next = l1
            l1 = l1.next
            curr = curr.next

            curr.next = l2
            l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        

