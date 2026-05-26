# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left     # left 指向左子树（可以是 TreeNode 或 None）
#         self.right = right   # right 指向右子树（可以是 TreeNode 或 None）

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        翻转二叉树（把每个节点的左右子树交换）
        输入：root（树的根节点）
        输出：翻转后的树的根节点（和链表返回 head 一样的概念）
        """

        # ① 递归的“出口”：如果 root 是 None，说明子树是空的，直接返回
        #    （这避免继续往下递归产生错误）
        if not root:
            return None

        # ② 交换当前节点的左右孩子
        #    先暂存左孩子，然后把右孩子放到左边，再把左孩子放到右边
        
        root.left,root.right = root.right,root.left
      

        # ③ 递归处理新的左子树（原来的右子树）
        self.invertTree(root.left)

        # ④ 递归处理新的右子树（原来的左子树）
        self.invertTree(root.right)

        # ⑤ 返回当前节点根 root（非常重要！必须返回整个树的入口）
        #    就像链表操作返回 head 一样，树翻转后必须把根节点交还给调用者
        return root
