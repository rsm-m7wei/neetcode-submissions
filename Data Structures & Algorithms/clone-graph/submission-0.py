"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node, visited):
      
        if node in visited:
            return visited[node]
        copy_node=Node(node.val)
        visited[node]=copy_node
        for neighbor in node.neighbors:
            copy_node.neighbors.append(self.dfs(neighbor,visited))
        return copy_node



    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return  
        visited ={} 
        return self.dfs(node,visited)