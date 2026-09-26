# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def treetrav(root):
            if not root:
                return None
            temp = root.right 
            root.right =root.left
            root.left= temp
            treetrav(root.left)
            treetrav(root.right)
            return root
        
        return treetrav(root)
        