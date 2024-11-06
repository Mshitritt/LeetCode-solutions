"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path = []
        q_path = []
        q_copy = q
        
        while q:
            if q.parent:
                q_path.append(q.parent)
                q = q.parent
                if q.val == p.val:
                    return p
            else:
                break
        q = q_copy
        while p:
            if p.parent:
                p_path.append(p.parent)
                p = p.parent
                if p.val == q.val:
                    return q
            else:
                break
        
        
        

        ans = None
        i = -1
        if len(p_path) > 0 and len(q_path) > 0:
            while p_path[i] == q_path[i]:
                ans = p_path[i]
                i -= 1
                if i < -len(p_path) or i < -len(q_path):
                    return ans
        
        return ans 

        

            