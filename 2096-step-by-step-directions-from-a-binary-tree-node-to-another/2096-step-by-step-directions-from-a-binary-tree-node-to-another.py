# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path_s = []
        path_d = []
        def helper(node, target, arr):
            if not node:
                return False
            if node.val == target:
                return True
                       
             
            if helper(node.left, target, arr):
                arr.append('L')
                return True
            if helper(node.right, target, arr):
                arr.append('R')
                return True
        
        helper(root, startValue, path_s)
        helper(root, destValue, path_d)

        path_s.reverse()
        path_d.reverse()

        anc = 0
        while path_s and path_d and anc < min(len(path_s), len(path_d)) and path_s[anc] == path_d[anc]:
            anc += 1

        res = ""
        # adding up
        for _ in range(len(path_s[anc:])):
            res += 'U'
        
        # adding directions
        for c in path_d[anc:]:
            res += c
        return res

                



        




       
       













