# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class TreeNode:
    #def __init__(self,val= 0, left =None, right =None):
        #self.val = val
        #self.left = left
        #self.right = right
class TreeeNode:
    def __inif__(self,val=0,left =None,right =None):
        self.val =val
        self.left =left
        self.right =right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            # if not preorder or not inorder:
            #     return None #这里返回的逻辑是要返回一个tree node，如果这里没有，这里返回的就是none，而不是true。
            # root =TreeNode(preorder[0]) # 做切片的时候直接用中括号就行，不用再加（）
            # dex = inorder.index(preorder[0])# 这里不能是root，因为你要的是一个index，而这里你返回的是一个tree node
            # root.left =self.buildTree(preorder[1:1+dex],inorder[:dex]) #接下来，你要相信递归，只想好这一层的功能就行：分开左右。
            # root.right = self.buildTree(preorder[1+dex:],inorder[dex+1:])
            # return root

            #这依旧是递归
            #首先是考虑基本情况，也就是不能活着不需要递归的情况：
            #两个里面有一个处理完了
            if not preorder or not inorder:
                return None
            #获取当前root!!!，放进树里面
            root = TreeNode(preorder[0])
            #在中序中找到位置，这个之前的就是左孩子，之后是root，之后是右孩子
            ind = inorder.index(preorder[0])
            #更新当前root的左右孩子,pre的树左孩子在中间
            root.left = self.buildTree(preorder[1:1+ind],inorder[:ind])
            root.right =self.buildTree(preorder[ind+1:],inorder[ind+1:])
            #每一层返回上一层的变量：
            return root




            
