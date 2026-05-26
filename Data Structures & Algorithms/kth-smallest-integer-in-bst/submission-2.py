# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

           
            # n=0
            # stack = []
            # curr =root # 用stack，来做dfs（从最后的一个取出来），需要一个计数器，一个list作为stack，一个指针，指向现在的node
            # while curr or stack:# 待处理和未录入的还有的时候就行
            #     while curr: #还没录入的先录入，一直往左到底
            #         stack.append(curr)
            #         curr =curr.left
            #     curr =stack.pop()# 左边结束了，接下来pop出中间的数字，
            #     n+=1 #计数告诉我现在处理了几个
            #     if n ==k: # 如果是对应的就返回
            #         return curr.val
            #     curr =curr.right # 左 中现在 到右边
        
        #！！！！递归的写法
        #需要全局记住k和用一个空的变量来存回答
        # self.k =k
        # self.res = None
        # def inorder(root):
        #     #基本情况的：到底或者找到了回答
        #     if not root or self.res is not None:
        #         return
        #     #本层处理完了，接下来开始递归，先递左边
        #     inorder(root.left)
        #     #因为找的是倒数，所以我们归的时候再处理
        #     self.k -=1
        #     if self.k ==0:
        #         #这里不要用append，要用=
        #         #！！在 Python 中，append 主要用于可变、有序容器（如 list、deque），用于将单个元素追加到末尾。
        #         self.res = root.val
        #     #接下来再处理右边
        #     inorder(root.right)
        # #写完了，我们开始初始化来调用函数
        # inorder(root)
        # return self.res


        #用stack来模拟递归做中序遍历
        stack =[]
        
        # 只要还能继续向左深入（root 非空）或还能回溯处理节点（stack 非空），遍历就未结束
        while stack or root:
            #当还没走到底的时候
            while root:
                stack.append(root)
                root =root.left
            #走到底之后开始归
            k -=1
            node =stack.pop()
            if k ==0:
                return node.val
            #!!!这里是最后把
            root =node.right



        




                

         