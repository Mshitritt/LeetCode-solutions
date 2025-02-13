# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, node: Optional[ListNode]) -> List[Optional[ListNode]]:
        slow = fast = node
        while fast.next != node:
            if fast.next.next == node:
                fast = fast.next
            else:
                fast = fast.next.next
                slow = slow.next
        
        fast.next = slow.next
        slow.next = node

        return (node, fast.next)
        """
        My solution but more clearly 
        -----------------------------------
        -- you can do with less logic -- 
        -- Check WHY is working ??? 

        def splitCircularLinkedList(self, node: Optional[ListNode]) -> List[Optional[ListNode]]:
            slow = fast = node
            while fast.next != node:
                if fast.next.next == node:
                    fast = fast.next
                else:
                    fast = fast.next.next
                    slow = slow.next
            
            fast.next = slow.next
            slow.next = node

            return (node, fast.next)
        -----------------------------------------
        """
        """
        if not list or not list.next:
            return [list, None]

        # Step 1: Find the length of the circular linked list
        length = 1
        current = list
        while current.next != list:
            current = current.next
            length += 1
        
        # Step 2: Use slow and fast pointer to find the middle
        mid = (length + 1) // 2  # This ensures ceil(length / 2)
        prev = None
        slow = list
        for _ in range(mid):  
            prev = slow
            slow = slow.next

        # Step 3: Break the circular list into two parts
        prev.next = list  # First half remains circular

        # Find the last node of the second half
        last = slow
        while last.next != list:
            last = last.next
        last.next = slow  # Second half remains circular

        return [list, slow]
        """
        

        