# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def mergeLists(self,l1,l2):
        dummy = ListNode()
        curr1,curr2 = l1,l2
        dummy_curr = dummy
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                dummy_curr.next = curr1
                curr1 = curr1.next
            else:
                dummy_curr.next = curr2
                curr2 = curr2.next
            dummy_curr = dummy_curr.next
        if curr1:
            dummy_curr.next = curr1
        if curr2:
            dummy_curr.next = curr2

        return dummy.next
    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        dummyList = lists[0] if lists[0] else None
        if not dummyList:
            return dummyList
        
        for i in range(1,len(lists)):
            dummyList = self.mergeLists(dummyList,lists[i])
        return dummyList


        