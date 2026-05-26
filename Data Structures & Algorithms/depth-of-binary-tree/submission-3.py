class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
                
        

        if not root: #考虑边缘情况，如果一个node都没有，这里就return0# 按照之前的规则，这里就要写成root
            return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
        # 如果这里有node的话，就想想返回给上一个母节点的内容可以是什么，这里就是1+（这个节点的深度本身）下一个！！！（这里就代表要用上递归）节点的最大深度


        