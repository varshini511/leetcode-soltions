# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum = curr_sum * 10 + node.val
            # If leaf node, return the number formed
            if not node.left and not node.right:
                return curr_sum
            # Otherwise, recurse left and right
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        
        return dfs(root, 0)

        