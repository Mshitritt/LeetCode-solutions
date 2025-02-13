"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)

        # Case 1: Empty List - Create a new single-node circular list
        if not head:
            node.next = node
            return node

        # Case 2: Single node - Insert new node to form circular link
        if head.next == head:
            head.next = node
            node.next = head
            return head

        prev, nxt = head, head.next
        while True:
            # Case 3: Insert in between two nodes where prev <= insertVal <= nxt
            if prev.val <= insertVal <= nxt.val:
                break
            
            # Case 4: Insert at the turning point (where prev > nxt)
            if prev.val > nxt.val:  
                if insertVal >= prev.val or insertVal <= nxt.val:
                    break

            # Move to the next node
            prev, nxt = nxt, nxt.next

            # If we've gone full circle, insert anywhere
            if prev == head:
                break
        
        # Insert new node
        prev.next = node
        node.next = nxt
        return head
        

        



        