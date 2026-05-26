class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        在二叉搜索树（BST）中找到两个节点 p 和 q 的最近公共祖先（LCA）。
        
        BST 的特性：
            - 左子树所有节点 < 当前节点
            - 右子树所有节点 > 当前节点
        
        因此：
            - 如果 p 和 q 都比当前节点小 → LCA 在左子树
            - 如果 p 和 q 都比当前节点大 → LCA 在右子树
            - 否则（分叉） → 当前节点就是 LCA
        """

        # curr = root   # 从根节点开始往下搜索

        # while curr:
        #     # 情况 1：p 和 q 都在当前节点的左边
        #     if p.val < curr.val and q.val < curr.val:
        #         curr = curr.left      # 往左走

        #     # 情况 2：p 和 q 都在当前节点的右边
        #     elif p.val > curr.val and q.val > curr.val:
        #         curr = curr.right     # 往右走

        #     # 情况 3：p 和 q 分别在当前节点两侧（或其中一个就是 curr）
        #     #         那么当前节点就是最近公共祖先
        #     else:
        #         return curr           # 找到 LCA
        
        # # 理论上不会走到这里（BST 必然能找到 LCA）
        # return None

        if root.val<q.val and root.val<p.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val>q.val and root.val>p.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
