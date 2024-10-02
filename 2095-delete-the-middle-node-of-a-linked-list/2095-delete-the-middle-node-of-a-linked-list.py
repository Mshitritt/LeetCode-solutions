# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0 
        head_copy = head
        while head:
            count += 1
            head = head.next
        
        mid = count // 2
        if mid == 0:
            return head_copy.next
        
        prev = head_copy
        curr = prev.next
        mid -= 1
        while curr:
            if mid != 0:
                prev = curr
                curr = curr.next
                mid -= 1
            else:
                prev.next = curr.next
                return head_copy