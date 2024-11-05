# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        rTl = True
        q = deque([root])

        while q:
            lvl_size = len(q)
            lvl = []

            for _ in range(lvl_size):
                curr = q.popleft()
                lvl.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            if not rTl:
                lvl.reverse()

            res.append(lvl)
            rTl = not rTl
        
        return res