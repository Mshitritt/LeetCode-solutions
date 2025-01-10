# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.nodes = []
        # inorder traversal
        
        def rec(node):
            if not node:
                return
            
            rec(node.left)
            self.nodes.append(node.val)
            rec(node.right)
            
        rec(root)

        for i in range(1, len(self.nodes)):
            if self.nodes[i-1] >= self.nodes[i]:
                return False
        return True
