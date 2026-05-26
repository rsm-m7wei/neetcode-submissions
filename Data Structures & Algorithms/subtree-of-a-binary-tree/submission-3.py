class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        判断 subRoot 是否是 root 的一个子树。
        整体思路：
        1. 在 root 这棵大树中，不断往下搜索“可能的起点”
        2. 一旦某个节点值和 subRoot 匹配，就调用 sametree 检查两棵树是否完全相同
        3. 如果当前节点不匹配，则继续在左子树 / 右子树中继续搜索
        """

        # # 情况 1：subRoot 为空 → 空树永远是任何树的子树
        # if not subRoot:
        #     return True

        # # 情况 2：root 为空，但 subRoot 不空 → 不可能匹配
        # if not root:
        #     return False

        # # 情况 3：以当前 root 为根的这棵树，如果与 subRoot 完全相同 → 直接返回 True
        # if self.sametree(root, subRoot):
        #     return True

        # # 情况 4：否则，在左子树 / 右子树里继续递归搜索 subRoot
        # return (self.isSubtree(root.left, subRoot) or 
        #         self.isSubtree(root.right, subRoot))


        #特殊情况
        if not subRoot:
            return True
        if not root:
            return False
        #接着检查从这个节点开始是不是能一样，不一样的话看下面的左右两个节点开始一不一样，子节点其中一个一样也呢个酸痛哟，
        #所以这用or
        if self.sametree(root,subRoot):
            return True
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)




    def sametree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t and not s:
            return True
        if not t or not s or t.val != s.val:
            return False
        #如果都不是以上两种情况，就代表这一个节点是完全相同的，我们就接着检查左右两个节点
        return self.sametree(s.right,t.right) and self.sametree(s.left,t.left)

        # """
        # 判断两棵树是否从当前节点开始完全相同。
        # 只做“比较”，不负责“到处找起点”。
        # """

        # # 情况 1：两边都空 → 这条分支结构完全相同
        # if not s and not t:
        #     return True

        # # 情况 2：一个空一个不空，或者值不一样 → 不可能相同
        # if not s or not t or s.val != t.val:
        #     return False

        # # 情况 3：当前节点值相同，继续比较左右子树
        # # 只有左右子树都相同，整棵树才算相同
        # return (self.sametree(s.left, t.left) and 
        #         self.sametree(s.right, t.right))
