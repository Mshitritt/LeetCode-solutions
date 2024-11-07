# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def isExist(root, target):
            if not root:
                return False
            if root.val == target.val:
                return True
            
            left = isExist(root.left, target)
            right = isExist(root.right, target)

            return left or right
        
        def lca(root, p, q):
            if not root:
                return None
            if (root.val == p.val) or (root.val == q.val):
                return root
            
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            if left and right:
                return root
            else:
                return left if left else right
        
        if not isExist(root, p) or not isExist(root, q):
            return False
        else:
            return lca(root, p, q)
            
            


            