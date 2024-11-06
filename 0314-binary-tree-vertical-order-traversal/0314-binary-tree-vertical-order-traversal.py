# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        groups = {}
        col = 0
        row = 0
        q = deque()
        q.append((root, row, col))
        while q:
            curr = q.popleft()
            node = curr[0]
            r = curr[1]
            c = curr[2]
            if c in groups:
                groups[c].append(node.val)
            else:
                groups[c] = [node.val]
            if node.left:
                q.append((node.left, r+1, c-1))
            if node.right:
                q.append((node.right, r+1, c+1))

        sorted_columns = sorted(groups.keys())
        res = [groups[col] for col in sorted_columns]
        
        return res
            

