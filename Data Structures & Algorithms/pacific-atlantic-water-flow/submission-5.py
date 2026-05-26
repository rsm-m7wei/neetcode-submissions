class Solution: #总的来说这一个题目的思考放方法是倒过来，懂两个海洋能淹没到什么地方，再重叠，来思考那些地方能流向海洋
    # def dfs(self,r,c,heights,ocean):
    #     ocean[r][c] =True #每走到一个地方，首先把这里的位置标记成true
    #     lst = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
    #     for i, j in lst: # 之后对于上下左右的位置，如果在棋盘里面，并且之前没到达过，并且高度大于！！或者等于上一个点，则移动到下一个点进行递归
    #         if i >=0 and i<len(heights) and j>=0 and j<len(heights[0]) and not ocean[i][j] and heights[i][j]>=heights[r][c]:
    #             self.dfs(i,j,heights,ocean)
    #     return

    #写一个dfs来看海水能蔓延到哪里
    def dfs(self,c,r,heights,ocean):
        #基本情况，如果不在界内，或者这个地方比上一个个子高，海水流不过来，就不用递归，直接return，一以下简略
        
        #之后对是处理当前状态,走到一个地方就把这个地方设置成true
        ocean[r][c]=True
        #枚举下一步要处理的cell
        lst =[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
        #对里面的每一个情况进行判断，如果在界内，且满足高度要求就进行下一步的dfs. !!!注意这里要确保去的格子是false,也就是没去过的地方。
        for i,j in lst:
            if i>=0 and i<len(heights) and j>=0 and j<len(heights[0]) and not ocean[i][j] and heights[i][j]>=heights[r][c]:
                self.dfs(j,i,heights,ocean)
        return
        
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # res = []
        # row =len(heights) # 创建返回的空列表，之后创建全是false的对应矩阵，之后对
        # colum = len(heights[0])
        # paci = [[False for i in range(colum)] for j in range(row)]
        # atla = [[False for i in range(colum)] for j in range(row)]
        # for i in range(row):
        #     #对竖的左右两行进行检验，从他们来看是否能到达,我们需要能确认定位到height和atla的具体格子，所以我们需要横纵坐标，需要连个棋盘的传入
        #     self.dfs(i, colum-1,heights,atla)
        #     self.dfs(i, 0,heights,paci)
        # for i in range(colum): # 从竖的地方进行检验，看每个海洋能进行到哪里，并且把它们存到对应的全false矩阵之中
        #     self.dfs(0,i,heights,paci)
        #     self.dfs(row-1,i,heights,atla)
        # for i in range(row): #
        #     for j in range(colum):# 对于对应矩阵的每一个元素，如果两个的对应位置都是true，就把对应坐标加入到res里面
        #         if paci[i][j] and atla[i][j]:
        #             res.append([i,j])
        # return res # 最后返回res

        #首先我们初始变量来存放回答
        res =[]
        #创造两个 全false的grid
        rows = len(heights)
        cols = len(heights[0])
        pac = [[False for i in range(cols)] for j in range(rows)]
        atl = [[False for i in range(cols)] for j in range(rows)]

        #检查从左右，上下，能流向哪些cell (列，行，heights，海洋)
        for i in range(rows):
            self.dfs(0,i,heights,pac)
            self.dfs(cols-1,i,heights,atl)
        for j in range(cols):
            self.dfs(j,0,heights,pac)
            self.dfs(j,rows-1,heights,atl)
        #如果两个海洋的cell 都是true，则可以加入到res
        for i in range(rows):
            for j in range(cols):
                if pac[i][j] and atl[i][j]:
                    res.append([i,j])
        return res
        




