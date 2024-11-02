# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # implement using Pai array - fathers array    
        p_anc = []
        q_anc = []

        def helper(node, nodeTarget, arr):
            if node is None:
                return False
            if node.val == nodeTarget.val:
                arr.append(node)
                return True
            # Recur on the left and right children
            found_in_left = helper(node.left, nodeTarget, arr)
            found_in_right = helper(node.right, nodeTarget, arr)
            
            # If the target is found in either subtree, add this node to the path
            if found_in_left or found_in_right:
                arr.append(node)
                return True
            
            return False  # Return False if target is not found in either subtree
        
        helper(root, p, p_anc)
        helper(root, q, q_anc)
        
        i = -1
        n = min(len(p_anc), len(q_anc))
        # -3, -2, -1
        while i >= -n and p_anc[i].val == q_anc[i].val:
            i -= 1
        
        return p_anc[i+1]

        




        
            