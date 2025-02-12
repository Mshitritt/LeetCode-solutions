# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head

        # chaeck if k > len(list)
        n = 0
        el = head
        while el:
            n += 1
            el = el.next
        k = k % n if k >= n else k
        if k == 0:
            return head

        # find new tail and head
        k_newTail = n - k - 1
        newTail = head
        while k_newTail:
            newTail = newTail.next
            k_newTail -= 1
        newHead = newTail.next

        # swap the halfes 
        curr = newHead
        while curr and curr.next:
            curr = curr.next 
        newTail.next = None
        curr.next = head

        return newHead




        
