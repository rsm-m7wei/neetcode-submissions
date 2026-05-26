# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] #创建一个新的list来存放结果
        q = collections.deque() 
        q.append(root) #创建一个队列，队列左右可以O1删加，效率高,这里先把初始条件root加入进来
        while q:
            qlen= len(q) # 计算出后面会出现的队列的长度，不然下面会更改
            level =[] # 用一个list来存放这一层的信息，放着一层被处理完之后level会被清除，之后再给一个新的level
            for i in range(qlen):
                node= q.popleft()# 对于每一层的每一个元素，把这一层的信息从先到的地方pop出来，之后存到一个node里面，再把这个node里面的数值存放到这一层的list里面
                if node:
                    level.append(node.val) # 如果有node里面有内容就接到level里面，并且把子集给加入进去
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)# 这一整层！！的循环结束之后，对于每一层，如果有level有内容就嫁到res里面，下一次循环会给一新的空level
        return res


        res =[]
        q= collections.deque()
        q.appedn(root) #这里要维护一个队列来做bfs！！！用得到一个列表，一个队列，并初始化，就是先到的先出，储存每一层的信息，并且初始化root,
        while q:
            level =[]
            qlen =len(q) # 题目要求是list套list，那每一层再单独给一个list，并且要通过长度来遍历这一层的全部信息
            for i in range(qlen):
                node.q.popleft() #从这里面pop出来一个内容来遍历处理这一层的信息
                if node:
                    level.append(level)
                    q.append(q.left)
                    q.append(q.rihgt)
            if level:
                res.qppend(level) # 对于每一层处理完之后加到res里面
        return res

