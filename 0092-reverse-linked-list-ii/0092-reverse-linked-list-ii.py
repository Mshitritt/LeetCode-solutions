# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        values = deque()
        node = head
        nodeL = None
        while node:
            left -= 1
            if left == 0:
                nodeL = node
            if nodeL:
                values.append(node.val)
            if node.val == right:
                break
            node = node.next
            
        
        while values:
            nodeL.val = values.pop()
            nodeL = nodeL.next
        
        return head

            

        