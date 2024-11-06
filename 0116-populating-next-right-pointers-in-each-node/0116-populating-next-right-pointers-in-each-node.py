"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        count = 1
        q = deque([root])
        root.next = None
        while q:
            
            curr = q.popleft()
            lvl_size = len(q)
            nxt = None
            while lvl_size:
                nxt = q.popleft()
                curr.next = nxt
                if curr.left:
                    q.append(curr.left)
                    q.append(curr.right)
                curr = nxt
                lvl_size -= 1
            else:
                curr.next = None
                if curr.left:
                    q.append(curr.left)
                    q.append(curr.right)
        return root
                
