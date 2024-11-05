# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        count = 1
        while q:
            temp = []
            nxtCount = 0
            while count:
                curr = q.popleft()
                temp.append(curr.val)
                count -= 1
                if curr.left:
                    q.append(curr.left)
                    nxtCount += 1
                if curr.right:
                    q.append(curr.right)
                    nxtCount += 1
            res.append(temp)
            count = nxtCount
        
        return res
            
