# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # return the longest Zigzag path of direction
        # direction: 0-left, 1-right
        zigzag = 0  # Initialize a global variable to keep track of the longest ZigZag path

        def helper(node, direction, length):
            nonlocal zigzag
            if not node:
                return
            # Update the global ZigZag path length if this path is the longest so far
            zigzag = max(zigzag, length)
            
            # Continue the path in ZigZag fashion
            if direction == 0:  # Current direction is left, so go right next
                helper(node.left, 0, 1)           # Restart path from left child
                helper(node.right, 1, length + 1)  # Continue ZigZag by going right
            else:  # Current direction is right, so go left next
                helper(node.left, 0, length + 1)   # Continue ZigZag by going left
                helper(node.right, 1, 1)           # Restart path from right child

        # Start from the root with both left and right directions
        helper(root, 0, 0)  # Start with direction left
        helper(root, 1, 0)  # Start with direction right
        
        return zigzag

