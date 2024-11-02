# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counts = {0: 1}

        def helper(node, count):
            if node is not None:
                curr_sum = count + node.val
                
                # get all valid paths
                pathCounter = counts.get(curr_sum - targetSum, 0)
                
                # update the curr_sum into counts
                counts[curr_sum] = counts.get(curr_sum, 0) + 1

                # add the valid paths of sub tree
                pathCounter += helper(node.left, curr_sum) + helper(node.right, curr_sum)
                
                # backtrack - remove elements from counts 
                counts[curr_sum] -= 1
                if counts[curr_sum] == 0:
                    del counts[curr_sum]
                return pathCounter

            else:
                return 0
        
        return helper(root, 0)
        

            
