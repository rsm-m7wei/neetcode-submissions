# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,left,right): # 对于递归问题，这里现实简化问题，比如对于树，这里就先写一个helper fiction 来解决三个节点的树的问题
            if not node:
                return True # 这种都是先写一个true的条件，普遍都会是not node， 这代表已经遍历结束了，所有都符合要求
            if not(node.val<right and node.val>left): # 这个是中途不符合要求会推出的条件
                return False
            return (valid(node.left,left,node.val)and # 这个事中途符合条件，接下来往下递归的条件和改变
            valid(node.right,node.val,right))
        return valid(root,float('-inf'),float('inf')) # 这里调用函数（缩进减少），并且给出初始条件