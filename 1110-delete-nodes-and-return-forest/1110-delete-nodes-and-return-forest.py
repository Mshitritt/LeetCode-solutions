# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.res = []
        to_delete = set(to_delete)
        if not to_delete:
            return []
        if root.val not in to_delete:
            self.res.append(root)

        def dfs(node):
            if not node:
                return None
            
            
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            
            if node.val in to_delete:    
                if node.left:
                    self.res.append(node.left)
                if node.right:
                    self.res.append(node.right)
                return None
            else:
                return node
                

        dfs(root)
        return self.res
                
            
            
