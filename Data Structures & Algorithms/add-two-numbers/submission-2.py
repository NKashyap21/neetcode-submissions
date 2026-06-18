# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2=l1,l2
        carry=0
        dummy = ListNode(0)
        dummy_curr = dummy

        while curr1 and curr2:
            x = curr1.val + curr2.val + carry
            remainder = (x % 10) 
            carry = x//10
            dummy_curr.next = ListNode(remainder)

            curr1 = curr1.next
            curr2 = curr2.next
            dummy_curr = dummy_curr.next

        while curr1:
            x = curr1.val + carry
            remainder = (x%10) 
            carry = x // 10
            dummy_curr.next = ListNode(remainder)

            curr1 = curr1.next
            dummy_curr = dummy_curr.next

        while curr2:
            x = curr2.val + carry
            remainder = (x%10)
            carry = x // 10
            dummy_curr.next = ListNode(remainder)

            curr2 = curr2.next
            dummy_curr = dummy_curr.next
        
        if carry != 0:
            dummy_curr.next = ListNode(carry)

        return dummy.next