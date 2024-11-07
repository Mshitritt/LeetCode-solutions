# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            if not node.left and not node.right and node.val == 0:
                return 1
            if not node.left and not node.right and node.val == 1:
                return 0
            
            if node.val > 1:
                coins_chiled = helper(node.left) + helper(node.right)
                if node.val - coins_chiled -1 > 0:
                    return (node.val - coins_chiled-1) + coins_chiled
                return coins_chiled
            elif node.val == 1:
                return helper(node.left) + helper(node.right)
            else:
                return helper(node.left) + helper(node.right)
        return helper(root)


            