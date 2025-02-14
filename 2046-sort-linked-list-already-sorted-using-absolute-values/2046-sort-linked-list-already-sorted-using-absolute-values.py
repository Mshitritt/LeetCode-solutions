# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        
        neg, pos = ListNode(), ListNode()
        negHead, posHead = neg, pos
        curr = head
        while curr:
            temp = curr.next

            if curr.val < 0:
                neg.next = curr
                curr.next = None
                neg = neg.next
            else:
                pos.next = curr
                curr.next = None
                pos = pos.next
                
            curr = temp
        
        # REVERSE NEG
        negHead, posHead = negHead.next, posHead.next
        prev, curr = None, negHead
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # MERGE THE LISTS
        if negHead:
            negHead.next = posHead 
            return prev
        return posHead
        

