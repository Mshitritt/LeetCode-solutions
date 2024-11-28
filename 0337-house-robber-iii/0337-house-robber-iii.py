# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Helper function to return (not_robbed, robbed) for each node
        def dp(node):
            if not node:
                return (0, 0)  # (not_robbed, robbed)
            
            # Solve for left and right children
            left = dp(node.left)
            right = dp(node.right)
            
            # If the current node is not robbed, take the max of its children
            not_robbed = max(left) + max(right)
            
            # If the current node is robbed, its children can't be robbed
            robbed = node.val + left[0] + right[0]
            
            return (not_robbed, robbed)
        
        # Get the result from the root
        return max(dp(root))