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
            final.append(root.val)
            traverse(root.left, final)
            traverse(root.right, final)
            return final
        result = traverse(root, final)
        result.sort()

        return result[k-1]

        