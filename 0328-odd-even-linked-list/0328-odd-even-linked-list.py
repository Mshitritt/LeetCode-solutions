# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head_copy = head
        even = head
        odd = head.next
        odd_copy = odd
        while even:
            even.next = odd.next
            if even.next is None:
                break
            else:
                even = even.next
            odd.next = even.next
            if odd.next is None:
                break
            else:
                odd = odd.next

        even.next = odd_copy
        return head_copy


