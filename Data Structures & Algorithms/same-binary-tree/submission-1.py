# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
       
    #     if not p and not q:
    #         return True
    #     if not p or not q or p.val!= q.val:
    #         return False
    #     return(self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right))

        #两个都没有
        if not p and not q:
            return True
        elif not p or not q or p.val !=q.val:
            return False
        #判断完每一层的特殊情况和不通过的情况，我们接着就到下一层去递归
        return(self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))