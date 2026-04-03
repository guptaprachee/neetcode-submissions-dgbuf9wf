# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        final =[]
        def traverse(root, final):
            if not root:
                return 
            traverse(root.left, final)
            final.append(root.val)
            traverse(root.right, final)
            return final

        return traverse(root, final)[k-1]

        