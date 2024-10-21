# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        resSum = -float('inf')
        resLevel = 1
        level = 0
        if root.left is None and root.right is None:
            return 1
        while q:
            size = len(q)
            levelSum = 0
            level += 1
            for _ in range(size):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if levelSum > resSum:
                resSum = levelSum
                resLevel = level

        if levelSum > resSum:
            resSum = levelSum
        return resLevel

