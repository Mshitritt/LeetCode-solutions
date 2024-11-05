# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        res = []
        q = deque([root])
        left_to_right = True  # This flag will determine the order of appending values
        
        while q:
            lvl_size = len(q)
            lvl = []
            
            for _ in range(lvl_size):
                node = q.popleft()
                lvl.append(node.val)
                
                # Always add children from left to right
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Reverse the current level's result if we are in a right-to-left mode
            if not left_to_right:
                lvl.reverse()
            
            res.append(lvl)
            left_to_right = not left_to_right  # Toggle the order for the next level
        
        return res