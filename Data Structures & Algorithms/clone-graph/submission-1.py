"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node, visited):
      # 我们做这个函数就是为了复制，所以最后一定是返回一个copy的node
        if node in visited: # 如果已经在visited里面就直接返回visited的对于对象
            return visited[node]
        copy_node=Node(node.val) # 如果没有的话，就先copy一个出来，这里就是先制造一个val一样的节点，接下来在逐步处理neighbor
        visited[node]=copy_node # 复制出来之后加入到visited这个列表的对应位置
        for neighbor in node.neighbors: # 再对里面的neighbor（他们也是一个一个的node节点）来循环处理，
            copy_node.neighbors.append(self.dfs(neighbor,visited))
        return copy_node #！！！最后别忘了函数一定要返回东西



    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: # 这道题目还是图类型的递归，其实visited里面key和value都是Node类型
            return   #这里还是处理边界情况，没有的情况下什么都不需需要返回
        visited ={}  # 我们怎么知道访问了哪些节点？就把原来的node作为key，对应复制的node作为value（也有value，和neighbors两个属性）
        return self.dfs(node,visited) # 接下来就是调用dfs函数