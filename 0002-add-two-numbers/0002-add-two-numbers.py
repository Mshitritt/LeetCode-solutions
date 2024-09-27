# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = l1
        curr = head
        while l1 or l2:
            if l1 and l2:
                sum_val = l1.val + l2.val + carry
                if sum_val >= 10:
                    copy_sum_val = sum_val
                    sum_val = sum_val % 10
                    carry = (copy_sum_val - sum_val) // 10
                else:
                    carry = 0
                l1.val = sum_val

                if l1.next is None:
                    curr = l1
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum_val = l1.val + carry
                if sum_val >= 10:
                    copy_sum_val = sum_val
                    sum_val = sum_val % 10
                    carry = (copy_sum_val - sum_val) // 10
                else:
                    carry = 0
                l1.val = sum_val
                if l1.next is None:
                    curr = l1
                l1 = l1.next
            else:
                # list2 only
                sum_val = l2.val + carry
                if sum_val >= 10:
                    copy_sum_val = sum_val
                    sum_val = sum_val % 10
                    carry = (copy_sum_val - sum_val) // 10
                else:
                    carry = 0

                temp = ListNode(sum_val)
                temp.next = None
                curr.next = temp
                curr = curr.next
                l2 = l2.next

        if carry:
            temp = ListNode(carry)
            temp.next = None
            curr.next = temp

        return head

                

                




            
