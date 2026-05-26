# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
    
        res = [root.val] #起始一个位置 ！！！！这里写到列表的时候一定要把[0]写上，这样才能输出数字，不然就是列表
        def maxpath(root): # 用辅助函数来做递归
            if not root:
                return 0  # 这个时候我们可以把这个tree简化成只有三个点，到那时对里面的起始点，我们要写成root
                # 对于里面的分枝点，我们要在root.left这外面再套上一个自己的函数，这就代表是递归走到底找到的这个分枝点
            leftmax = max(0, maxpath(root.left))
            rightmax = max(0,maxpath(root.right))
            res[0] =max(res[0],root.val+leftmax+rightmax) # 更新目前可能的最大和
            return max(leftmax,rightmax)+root.val # 我们这个节点能个给母节点的最大和更新
        maxpath(root) # 调用函数，以root为起点遍历一遍，之后return 列表的第一个，就是我们的答案
        return res[0]




