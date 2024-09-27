# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to start the result list
        current = dummy     # Pointer to build the result list
        carry = 0           # Initialize carry to 0

        # Traverse both linked lists
        while l1 or l2 or carry:
            # Get the current values, or 0 if the list has been fully traversed
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10

            # Create a new node for the current sum and attach it to the result list
            current.next = ListNode(total)
            current = current.next

            # Move to the next nodes in the input lists if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

                

                




            
