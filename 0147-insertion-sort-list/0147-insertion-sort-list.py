# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        # each iteration we swap between curr and min value 
        curr = head
        while curr:
            nxt = curr.next
            minVal = curr
            while nxt:
                if nxt.val < minVal.val:
                    minVal = nxt 
                nxt = nxt.next
            if minVal != curr:
                # swap
                curr.val, minVal.val = minVal.val, curr.val
            curr = curr.next
        return head
        

        