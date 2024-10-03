# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # count the leangth of list
        count = 0
        head_copy = head

        while head:
            count += 1
            head = head.next
        if count == 2:
            return head_copy.val + head_copy.next.val
        mid = (count + 1) // 2
        mid_c = mid
        # revers the second half
        prev = head_copy
        curr = prev.next
        while curr:
            if mid > 0:
                prev = curr
                curr = prev.next
            else:
                temp = curr.next
                curr.next = prev
                prev = curr
                if temp is None:
                    break
                curr = temp

            mid -= 1

        # search for max sun twin
        max_twin = -float('inf')
        curr_right = curr
        curr_left = head_copy
        while mid_c > 0:
            max_twin = max(max_twin, curr_right.val + curr_left.val)
            mid_c -= 1
            curr_right = curr_right.next
            curr_left = curr_left.next

        return max_twin

        
