class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #首先初始化每一个节点的parent，默认的parent就是自己
        #接着，我们计算每一个节点的rank（类似于树的高度，）我们后续可以吧矮的树接到高的树上面，这样子我们，就可以更高效
        par =[ i  for i in range(n)]
        rank =[1]* n
        # 接下来我们定义一个能找到root的函数,输入是当前节点
        def find(n1):
            #默认的节点的的parent就是自己，所以
            res =n1
            #这里我们设定的就是root 节点的parent就是自己，如果不是的话，我们需要接着找,是的话我们就直接返回就行
            while res != par[res]:
                # 对整条树进行压缩
                par[res] =par[par[res]]
                #不是的话我们就把当前的指针移动到他的父亲那
                res =par[res]
            return res
        #对两个节点进行连接
        def union(n1,n2):
            #首先我们要找到两个节点的root，如果是一样的就不用union，因为就在一棵树上
            p1,p2 = find(n1),find(n2)
            if p1 ==p2:
                return 0
            #如果不一样的话，就把小的树接到大的树上边，并且更新rank
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p2] += rank[p1]
            else:
                par[p2] =p1
                rank[p1]+= rank[p2]
            return 1
        #
        res = n
        for n1, n2 in edges:
            res  -=union(n1,n2)
        return res


