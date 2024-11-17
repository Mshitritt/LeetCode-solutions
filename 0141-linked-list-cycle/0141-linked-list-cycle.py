# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        def cycle(node):
            if not node:
                return False

            if node.val == float('inf'):
                return True 
            
            node.val = float('inf')
            return cycle(node.next)
        return cycle(head)
            