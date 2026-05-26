class Solution:

    def dfs(self, i, j, grid):
       
        if i >=0 and  i<len(grid) and j>=0 and j<len(grid[i]) and grid[i][j] =='1':
            grid[i][j] = '0'
            self.dfs( i+1, j, grid)
            self.dfs( i-1, j, grid)
            self.dfs( i, j+1, grid)
            self.dfs( i, j-1, grid)
        else:
            return

        


        

    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0 #最最最开始，它希望返回数量，我们直接给他写一个0就行
        for i in range(len(grid)):
            for j in range(len(grid[i])): # 首先还是遍历每一个单位，看哪里满足条件，能成为起始点
                if grid[i][j] == '1':
                    self.dfs(i,j,grid) # 对其实点进行dfs，这个的目的扩散，把这一整块的island给淹没，这样就不会重复标记
                    island +=1 #全淹没了以后再计数加一
        return island


        