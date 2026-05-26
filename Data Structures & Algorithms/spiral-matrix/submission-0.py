class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #我们分别写向右，下，左，上移动的四个条件，并且满足基本条件，也就是在矩阵之内
        #首先初始化边界条件
        minrow = mincol=0
        maxrow =len(matrix)
        maxcol = len(matrix[0])
        row =0

        res =[]

        #确立while的条件：
        while minrow < maxrow and mincol <maxcol:

            #向右,之前已经初始化过row，这里只更新col
            for col in range(mincol, maxcol):
                res.append(matrix[row][col])
            #全部遍历完之后更新边界条件
            minrow +=1
            
            #python的特性，这里的col在遍历完之后会保留最后一个数值，也就是最右边
            #向下
            for row in range(minrow,maxrow):
                res.append(matrix[row][col])
            maxcol -=1
            # 走完 right / down 后边界已收缩，可能只剩一行或一列；
            # 必须再次检查边界，避免 left / up 重复访问或越界
            #向左!!range是包含起点，不包含终点，所以要-1，最后的-1代表向左走
            if minrow<maxrow and mincol <maxcol:
                for col in range(maxcol-1,mincol-1,-1):
                    res.append(matrix[row][col])
                maxrow -=1
                #向上
                for row in range(maxrow-1,minrow-1,-1):
                    res.append(matrix[row][col])
                mincol +=1
        return res


            

