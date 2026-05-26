class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # ❌ 这里缩进少了一个空格（或者一个 Tab），和上面的 if 不在同一层，导致 IndentationError
        #    def 下面这一层应该统一 4 个空格缩进
        #       vvvv 正确应该对齐到这里
        stack = [[root, 1]]      # ✅ 正确写法：缩进对齐 + 中间加空格更规范

        # ❌ 同样问题：res 这行也少了缩进
        #    必须和 stack 在同一缩进层级
        res = 1                  # ✅ 逻辑上可以是 0 或 1，一般写 0 也没问题

        # ❌ while 这一行也要和 stack/res 对齐
        while stack:             # ✅ 正确缩进：和上面的 stack、res 一样
            # ❌ 这一行也要多缩进 4 个空格，表示“属于 while 里面”
            node, depth = stack.pop()   # ✅ 解包成 node 和 depth

            # ⚠️ 你这里立刻写了一次 res = max(res, depth)，下面 if 里又写一次，完全没必要
            # res = max(res, depth)     # ❌ 可以删掉这一行，统一放到 if node: 里面

            if node:
                # ✅ 只在 node 不为 None 的时候更新深度即可
                res = max(res, depth)

                # ❌ 这里写成 root.left / root.right 是错的：
                #    你每次都只从“根节点”的左右孩子往下走，
                #    而不是从“当前节点 node”的左右孩子走。
                #    这样会导致始终只在根附近打转，遍历不到整棵树。
                # stack.append([root.left, depth + 1])
                # stack.append([root.right, depth + 1])

                # ✅ 正确应该是用 node 的左右孩子
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        # ❌ 你原来把 return res 写在 while 的缩进里面：
        #     这样 while 第一次循环刚结束就直接 return，根本没遍历完整棵树。
        #     return 必须和 while 对齐，表示“循环结束后再返回”。
        return res               # ✅ 放在 while 外面，代码才会遍历所有节点后再返回最大深度
