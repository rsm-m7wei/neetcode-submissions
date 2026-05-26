# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def valid(self, root, left, right):
        if not root:
            return True
        if not (root.val<right and root.val>left):
            return False
        return (self.valid(root.left, left,root.val) and self.valid(root.right, root.val,right))

            

            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'),float('inf'))
    