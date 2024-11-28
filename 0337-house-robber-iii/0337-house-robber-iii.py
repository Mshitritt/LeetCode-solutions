# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        
        def dp(node):
            if not node:
                return 0
            if node in memo:
                return memo[node]
            
            # Rob this node
            rob = node.val
            if node.left:
                rob += dp(node.left.left) + dp(node.left.right)
            if node.right:
                rob += dp(node.right.left) + dp(node.right.right)
            
            # Do not rob this node
            not_rob = dp(node.left) + dp(node.right)
            
            # Store the result
            memo[node] = max(rob, not_rob)
            return memo[node]
        
        return dp(root)