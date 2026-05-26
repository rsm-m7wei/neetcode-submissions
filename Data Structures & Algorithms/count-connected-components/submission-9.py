class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #这个思路是并查集，我们关心的就是每个edge里面的元素是不是同一组，如果不是我们就合并成一组，并且我们通过判断是不是同一个root来确定是不是同一组
        #首先我们要初始化，每个节点各自一组他就是自己的parent，并且他们的大小
        par =[ i for i in range(n)]
        rank = [1]*n
        
        #首先初始化每一个节点的parent，默认的parent就是自己
        #接着，我们计算每一个节点的rank（类似于树的高度，）我们后续可以吧矮的树接到高的树上面，这样子我们，就可以更高效
        # par =[ i  for i in range(n)]
        # rank =[1]* n

        #写一个函数能在一个group里面找到他们的root，我们最开始不是假设自己是自己的root么？但是连在一起就不是了
        def find(n1):
            res=n1
            while res != par[res]:
                #这一步是优化
                par[res]=par[par[res]]
                res = par[res]
            return res
        # 接下来我们定义一个能找到root的函数,输入是当前节点
        # def find(n1):
        #     #默认的节点的的parent就是自己，所以
        #     res =n1
        #     #这里我们设定的就是root 节点的parent就是自己，如果不是的话，我们需要接着找,是的话我们就直接返回就行
        #     while res != par[res]:
        #         # 对整条树进行压缩
        #         par[res] =par[par[res]]
        #         #不是的话我们就把当前的指针移动到他的父亲那
        #         res =par[res]
        #     return res
        #对两个节点进行连接


        #接下来我们写函数来处理两个节点，不在一组就合并（小的加入大的），在的话就跳过

        def union(n1,n2):
            #首先取到两个组的root（组长）
            p1,p2 = find(n1),find(n2)
            if p1== p2:
                return 0
            if rank[p1]>rank[p2]:
                rank[p1] +=rank[p2]
                par[p2] =p1
            else:
                rank[p2]+=rank[p1]
                par[p1]=p2
            return 1
            
        # def union(n1,n2):
        #     #首先我们要找到两个节点的root，如果是一样的就不用union，因为就在一棵树上
        #     p1,p2 = find(n1),find(n2)
        #     if p1 ==p2:
        #         return 0
        #     #如果不一样的话，就把小的树接到大的树上边，并且更新rank
        #     if rank[p2]>rank[p1]:
        #         par[p1]=p2
        #         rank[p2] += rank[p1]
        #     else:
        #         par[p2] =p1
        #         rank[p1]+= rank[p2]
        #     return 1
        

        #初始化每个节点都是自己一组
        res= n
        #通过处理每一个edge来更新有多少组
        for n1,n2 in edges:
            res -=union(n1,n2)
        return res
        # res = n
        # for n1, n2 in edges:
        #     res  -=union(n1,n2)
        # return res




        #！！！！以上是并查集做法（union set），以下是dfs做法

        # class Solution:
        #     def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #         # 特殊情况：如果只有一个节点，那一定只有 1 个连通分量
        #         if n == 1:
        #             return 1

        #         # 用来统计连通分量的数量
        #         components = 0

        #         # 构建邻接表（无向图）
        #         # graph[node] = 和 node 直接相连的所有节点
        #         graph = {node: [] for node in range(n)}

        #         # 根据 edges 填充邻接表
        #         for node1, node2 in edges:
        #             graph[node1].append(node2)
        #             graph[node2].append(node1)

        #         # 记录已经访问过的节点，避免重复遍历
        #         visited = set()

        #         # 定义 DFS 函数：从某个节点出发，
        #         # 把它所在的整个连通分量里的节点都标记为 visited
        #         def dfs(node):
        #             for neighbor in graph[node]:
        #                 if neighbor not in visited:
        #                     visited.add(neighbor)
        #                     dfs(neighbor)

        #         # 遍历所有节点
        #         for node in graph:
        #             # 如果这个节点已经被访问过，说明它已经属于某个连通分量
        #             if node in visited:
        #                 continue
        #             else:
        #                 # 发现一个新的连通分量
        #                 visited.add(node)
        #                 components += 1
        #                 # 从这个节点开始 DFS，标记整个连通块
        #                 dfs(node)

        #         # 返回连通分量总数
        #         return components



