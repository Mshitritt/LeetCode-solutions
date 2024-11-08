# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        self.head_copy = head
        def dfs(node, head):
            if not head:
                return True
            if not node:
                return False
            
            left = None
            right = None

            if node.val == head.val:
                if node.left and node.left.val == node.val:
                    left = dfs(node.left, head.next) or dfs(node.left, self.head_copy)
                else:
                    left = dfs(node.left, head.next)
                if node.right and node.right.val == node.val:
                    right = dfs(node.right, head.next) or dfs(node.right, self.head_copy)
                else:
                    right = dfs(node.right, head.next)
            else:
                left = dfs(node.left, self.head_copy)
                right = dfs(node.right, self.head_copy)

            return left or right
        
        return dfs(root, head)