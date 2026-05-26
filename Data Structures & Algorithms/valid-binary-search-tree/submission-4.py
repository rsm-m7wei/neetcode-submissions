# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def valid(self, root, left, right):
        # if not root:
        #     return True
        # if not (root.val<right and root.val>left):
        #     return False
        # return (self.valid(root.left, left,root.val) and self.valid(root.right, root.val,right))

        #首先是基本情况如果走到底会遇到的
        if not root:
            return True
        #如果当前不满足的话
        if not (root.val>left and root.val<right):
            return False
        #递归到下一层
        return (self.valid(root.left,left,root.val) and self.valid(root.right,root.val,right))
            

            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.valid(root, float('-inf'),float('inf'))
        return self.valid(root, float('-inf'),float('inf'))
    