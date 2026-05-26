class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #这道题把矩阵分割成第一行 or 第一列和剩下的，0出现在这两部分要分开处理
        #如果出现在第一行or 第一列，我们就在额外的注释点上打出来，
        #若在剩余部分则在第一行和第一列对应位置打出0来
        #在第二次遍历的时候我们再处理这些标记


        #首先我们额外定义一个变量 记录第一行or 第一列是否有0
        firstrow  =False
        firstcol = False
        #遍历里面的每一个元素
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                #如果是0我们再处理
                if matrix[row][col] ==0:
                    if row ==0:
                        firstrow =True
                    if col ==0:
                        firstcol =True
                    elif row!= 0 and col != 0:
                         matrix[row][0] = 0
                         matrix[0][col] =0
        #以上是完成了第一遍遍历，我们放入了0，完成对0状态的分析
        #接着我们第二遍遍历来进行处理
        #首先我们处理里面，因为先处理第一行or 第一列的话全是0 就丢失信息来
        for row in range(1, len(matrix)):
            for col in range(1,len(matrix[0])):
                #如果第一行 or 列 有0 则为0
                if matrix[0][col] == 0 or matrix[row][0]==0:
                    matrix[row][col] =0
        #处理外围
        #如果第一行有0，全换成0
        if firstrow :
            matrix[0] = [0]*len(matrix[0])
        #如果第一列有0 全换成0
        if firstcol:
            for i in range(len(matrix)):
                matrix[i][0]=0
            

