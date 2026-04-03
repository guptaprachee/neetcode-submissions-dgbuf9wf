# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count =0

        def dfs(root, count):
            if not root:
                return count
            count= 1+ max(dfs(root.left, count), dfs(root.right, count))
            return count
        return dfs(root, count)

        