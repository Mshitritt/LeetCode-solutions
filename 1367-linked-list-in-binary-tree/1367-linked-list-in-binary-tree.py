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
        """
        the first solution is my solution 
        the second solution might br more efficient 
        """
        """
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
        """
        # Helper function to match the linked list with a downward path
        def match_path(node, head):
            if not head:  # If we reach the end of the linked list, return True
                return True
            if not node:  # If the tree node is None, return False
                return False
            if node.val != head.val:  # If values do not match, return False
                return False
            # Recurse on left and right subtrees
            return match_path(node.left, head.next) or match_path(node.right, head.next)

        # Main function to traverse the tree
        def dfs(node):
            if not node:  # If the node is None, return False
                return False
            # Check if the current node starts a matching path
            if match_path(node, head):
                return True
            # Recurse on left and right subtrees
            return dfs(node.left) or dfs(node.right)

        # Start the DFS traversal from the root
        return dfs(root)