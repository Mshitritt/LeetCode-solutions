"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # mapping 
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val, None, None)
            curr = curr.next

        # connect the nodes
        curr = head
        while curr:
            newCurr = old_to_new[curr]
            newCurr.next = old_to_new[curr.next] if curr.next else None
            newCurr.random = old_to_new[curr.random] if curr.random else None
            curr = curr.next
        return old_to_new[head]
        