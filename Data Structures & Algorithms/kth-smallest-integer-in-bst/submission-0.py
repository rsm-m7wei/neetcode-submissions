# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

           
            n=0
            stack = []
            curr =root # 用stack，来做dfs（从最后的一个取出来），需要一个计数器，一个list作为stack，一个指针，指向现在的node
            while curr or stack:# 待处理和未录入的还有的时候就行
                while curr: #还没录入的先录入，一直往左到底
                    stack.append(curr)
                    curr =curr.left
                curr =stack.pop()# 左边结束了，接下来pop出中间的数字，
                n+=1 #计数告诉我现在处理了几个
                if n ==k: # 如果是对应的就返回
                    return curr.val
                curr =curr.right # 左 中现在 到右边
                

         