# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # include = True if prev node isn't got thief
        def rec(node, include):
            if not node:
                return 0
            
            if include:
                return node.val + rec(node.left, False) + rec(node.right, False)
            else:
                left = max(rec(node.left, True), rec(node.left, False))
                right = max(rec(node.right, True), rec(node.right, False))
                return left + right
        
        s1 = rec(root, True)
        s2 = rec(root, False)
        return max(s1, s2)